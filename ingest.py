"""
ingest.py - Ingestao de documentos: le arquivos, faz chunking (MARKDOWN),
gera embeddings e salva no Supabase.

PDFs sao convertidos para Markdown externamente via DeepSeek.
Para PDFs nao-convertidos, usa PyPDF2 como fallback basico.

Uso:
    py ingest.py                 # ingere apenas arquivos novos
    py ingest.py --force         # re-ingere todos os arquivos
    py ingest.py /caminho/docs   # diretorio customizado
"""

import argparse
import hashlib
import io
import ipaddress
import json
import logging
import random
import re
import socket
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import httpx
from langchain_text_splitters import MarkdownTextSplitter

import config
from rag import (
    create_document_embeddings,
    embedding_to_pgvector,
    supabase_delete,
    supabase_insert,
    supabase_select,
    supabase_update,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)
_last_embed_call_at = 0.0
_http_client: httpx.Client | None = None

# --- NOVAS FUNÇÕES DE LEITURA ---

def read_txt(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def read_pdf(filepath: str) -> str:
    """
    Le PDF usando PyPDF2 (fallback basico).
    Para melhor qualidade, converta PDFs para Markdown via DeepSeek
    e coloque o .md na pasta de documentos.
    """
    from PyPDF2 import PdfReader

    logger.info(f"Processando PDF com PyPDF2: {Path(filepath).name}")
    logger.info(
        "Dica: para melhor qualidade, converta o PDF para .md via DeepSeek "
        "e coloque na pasta de documentos."
    )

    try:
        reader = PdfReader(filepath)
        pages = []
        for page in reader.pages:
            text = page.extract_text()
            if text and text.strip():
                pages.append(text.strip())

        full_text = "\n\n".join(pages)

        if not full_text.strip():
            logger.warning(f"PyPDF2 retornou vazio para {filepath}")

        return full_text

    except Exception as e:
        logger.error(f"Erro ao ler PDF: {e}")
        raise e


def read_pdf_bytes(data: bytes) -> str:
    """
    Le PDF a partir de bytes usando PyPDF2.
    """
    from PyPDF2 import PdfReader

    reader = PdfReader(io.BytesIO(data))
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text and text.strip():
            pages.append(text.strip())
    return "\n\n".join(pages)

def read_docx(filepath: str) -> str:
    from docx import Document
    doc = Document(filepath)
    # Tenta manter uma estrutura minima de paragrafos
    return "\n\n".join(p.text for p in doc.paragraphs if p.text.strip())


READERS = {
    ".txt": read_txt,
    ".md": read_txt,
    ".csv": read_txt,
    ".json": read_txt,
    ".py": read_txt,
    ".js": read_txt,
    ".html": read_txt,
    ".xml": read_txt,
    ".pdf": read_pdf,   # PyPDF2 (fallback — prefira converter PDF → .md via DeepSeek)
    ".docx": read_docx,
}

# --- CHUNKING (singleton lazy do splitter) ---

_splitter: MarkdownTextSplitter | None = None


def _get_splitter() -> MarkdownTextSplitter:
    """Retorna instancia reutilizavel do MarkdownTextSplitter."""
    global _splitter
    if (
        _splitter is None
        or _splitter._chunk_size != config.CHUNK_SIZE
        or _splitter._chunk_overlap != config.CHUNK_OVERLAP
    ):
        _splitter = MarkdownTextSplitter(
            chunk_size=config.CHUNK_SIZE,
            chunk_overlap=config.CHUNK_OVERLAP,
        )
    return _splitter


def chunk_text(text: str) -> list[str]:
    """
    Usa MarkdownTextSplitter para respeitar a hierarquia do documento.
    """
    chunks = _get_splitter().split_text(text)

    if chunks:
        logger.info("Splitting gerou %d chunks. Exemplo do 1o chunk:\n%s...", len(chunks), chunks[0][:100])

    return chunks


# --- P1.2: Headers contextuais nos chunks ---

def _extract_heading_hierarchy(text: str) -> list[tuple[int, str, int]]:
    """Extrai headings Markdown com suas posicoes no texto.
    Retorna: [(nivel, texto_heading, posicao_char), ...]
    """
    headings = []
    for match in re.finditer(r'^(#{1,4})\s+(.+)$', text, re.MULTILINE):
        level = len(match.group(1))
        heading_text = match.group(2).strip()
        headings.append((level, heading_text, match.start()))
    return headings


def _get_heading_context_for_position(
    headings: list[tuple[int, str, int]],
    position: int,
) -> str:
    """Retorna a hierarquia de headings ativa em uma posicao do texto."""
    active: dict[int, str] = {}
    for level, heading_text, hpos in headings:
        if hpos > position:
            break
        active[level] = heading_text
        # Limpar headings mais profundos quando um mais alto aparece
        for deeper in list(active):
            if deeper > level:
                del active[deeper]

    if not active:
        return ""
    parts = [active[level] for level in sorted(active)]
    return " > ".join(parts)


def chunk_text_with_context(text: str, doc_title: str = "") -> list[str]:
    """Chunka texto e prepende contexto de headings a cada chunk."""
    raw_chunks = _get_splitter().split_text(text)
    headings = _extract_heading_hierarchy(text)

    if not headings or not raw_chunks:
        if raw_chunks:
            logger.info("Splitting gerou %d chunks (sem headings).", len(raw_chunks))
        return raw_chunks

    contextualized = []
    search_offset = 0
    for chunk in raw_chunks:
        # Encontrar posicao do chunk no texto original
        snippet = chunk[:80]
        pos = text.find(snippet, search_offset)
        if pos == -1:
            pos = search_offset
        else:
            search_offset = pos + len(chunk) // 2

        heading_ctx = _get_heading_context_for_position(headings, pos)

        prefix_parts = []
        if doc_title:
            prefix_parts.append(f"[{doc_title}]")
        if heading_ctx:
            prefix_parts.append(f"[{heading_ctx}]")

        if prefix_parts:
            prefix = " ".join(prefix_parts) + "\n\n"
            contextualized.append(prefix + chunk)
        else:
            contextualized.append(chunk)

    logger.info(
        "Splitting com contexto gerou %d chunks. Exemplo do 1o chunk:\n%s...",
        len(contextualized),
        contextualized[0][:150],
    )
    return contextualized


# --- P1.3: Inferencia de prioridade de documento ---

_PRIORITY_HIGH_PREFIXES = ("00-", "01-", "02-", "03-", "04-", "05-")
_PRIORITY_MEDIUM_NAMES = {
    "service-desk-processos.md",
    "service_desk_maxima_organizado.md",
    "glossario.md",
    "base-maxgestao.md",
    "artigos_base.md",
}


def _infer_priority(filename: str, chunk_count: int = 0) -> int:
    """Infere prioridade do documento: 10=core, 8=estruturado, 5=normal, 3=gigante."""
    lower = filename.lower()
    # Core MDs (00-05)
    if any(lower.startswith(p) for p in _PRIORITY_HIGH_PREFIXES) and lower.endswith(".md"):
        return 10
    # Documentos estruturados conhecidos
    if lower in _PRIORITY_MEDIUM_NAMES:
        return 8
    # Documentos gigantes que dominam resultados
    if chunk_count > 400:
        return 3
    return 5

# --- FIM DAS ALTERAÇÕES CRÍTICAS (O RESTO É MANTIDO PARA COMPATIBILIDADE) ---

def _is_quota_error(exc: Exception) -> bool:
    message = str(exc).lower()
    return "resource_exhausted" in message or "quota" in message or "429" in message


def _wait_for_embed_slot() -> None:
    global _last_embed_call_at
    min_interval = max(0.0, config.EMBEDDING_MIN_INTERVAL_SECONDS)
    if min_interval <= 0:
        return

    now = time.monotonic()
    wait_for = (_last_embed_call_at + min_interval) - now
    if wait_for > 0:
        time.sleep(wait_for)
    _last_embed_call_at = time.monotonic()


def _retry_delay_seconds(exc: Exception, attempt: int) -> float:
    message = str(exc)
    patterns = [
        r"retry in ([0-9]+(?:\.[0-9]+)?)s",
        r"retryDelay['\"]?:\s*['\"]([0-9]+)s['\"]",
    ]

    for pattern in patterns:
        match = re.search(pattern, message, flags=re.IGNORECASE)
        if match:
            base = float(match.group(1)) + 1.0
            jitter = random.uniform(0.0, max(0.0, config.EMBEDDING_RETRY_JITTER_SECONDS))
            return min(base + jitter, config.EMBEDDING_RETRY_MAX_SECONDS)

    backoff = config.EMBEDDING_RETRY_BASE_SECONDS * (2 ** (attempt - 1))
    jitter = random.uniform(0.0, max(0.0, config.EMBEDDING_RETRY_JITTER_SECONDS))
    return min(backoff + jitter, config.EMBEDDING_RETRY_MAX_SECONDS)


def _embed_batch_with_retry(contents: list[str], filename: str, first_chunk_index: int) -> list[list[float]]:
    for attempt in range(1, config.EMBEDDING_MAX_RETRIES + 1):
        try:
            _wait_for_embed_slot()
            return create_document_embeddings(contents)
        except Exception as exc:
            if not _is_quota_error(exc) or attempt == config.EMBEDDING_MAX_RETRIES:
                raise

            delay = _retry_delay_seconds(exc, attempt)
            logger.warning(
                "Gemini quota em %s (chunk %s, tentativa %s/%s). Aguardando %.1fs...",
                filename,
                first_chunk_index,
                attempt,
                config.EMBEDDING_MAX_RETRIES,
                delay,
            )
            time.sleep(delay)

    raise RuntimeError("Falha inesperada ao gerar embeddings")


def _load_failed_report(report_path: Path) -> dict:
    if not report_path.exists():
        return {"updated_at": None, "files": {}}

    try:
        with report_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict) and isinstance(data.get("files"), dict):
                return data
    except Exception as e:
        logger.warning("Erro ao carregar relatorio de falhas (%s): %s", report_path, e)

    return {"updated_at": None, "files": {}}


def _save_failed_report_entry(
    filename: str,
    source: str,
    total_chunks: int,
    failed_chunks: list[int],
    source_type: str = "file",
) -> None:
    report_path = Path(config.FAILED_INGEST_REPORT)
    report = _load_failed_report(report_path)
    files = report["files"]

    if failed_chunks:
        files[filename] = {
            "source": source,
            "source_type": source_type,
            "total_chunks": total_chunks,
            "failed_chunks": sorted(set(failed_chunks)),
        }
    else:
        files.pop(filename, None)

    report["updated_at"] = datetime.now(timezone.utc).isoformat()
    with report_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)


def _failed_sources_from_report() -> tuple[list[Path], list[str]]:
    report = _load_failed_report(Path(config.FAILED_INGEST_REPORT))
    file_sources: list[Path] = []
    url_sources: list[str] = []
    for entry in report.get("files", {}).values():
        source = entry.get("source")
        source_type = (entry.get("source_type") or "").lower()
        if not source:
            continue
        if source_type == "url" or _is_url(source):
            if _is_url(source):
                url_sources.append(source)
            continue
        source_path = Path(source)
        if source_path.exists() and source_path.suffix.lower() in READERS:
            file_sources.append(source_path)
    return file_sources, _dedupe_keep_order(url_sources)


def _get_indexed_filenames() -> set[str]:
    try:
        docs = supabase_select("documents", select="filename")
        return {doc["filename"] for doc in docs if doc.get("filename")}
    except Exception as e:
        logger.warning("Nao foi possivel consultar documentos existentes: %s", e)
        return set()


def _is_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
    except Exception:
        return False
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


# Redes privadas/reservadas bloqueadas para prevenir SSRF
_BLOCKED_NETWORKS = [
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),  # link-local / cloud metadata
    ipaddress.ip_network("0.0.0.0/8"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
]


def _is_private_url(url: str) -> bool:
    """Verifica se URL resolve para IP privado/reservado (protecao SSRF)."""
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return True
    try:
        addr = ipaddress.ip_address(socket.gethostbyname(hostname))
        return any(addr in net for net in _BLOCKED_NETWORKS)
    except (socket.gaierror, ValueError):
        return False


def _dedupe_keep_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            ordered.append(value)
    return ordered


def _to_slug(value: str, default: str = "source") -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "_", value).strip("_")
    return value or default


def _url_to_filename(url: str) -> str:
    parsed = urlparse(url)
    host = _to_slug(parsed.netloc.replace(":", "_"), default="web")
    path = parsed.path.strip("/")
    base = _to_slug(path.split("/")[-1] if path else "index", default="index")
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"url__{host}__{base}__{digest}"


def _title_from_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.path and parsed.path != "/":
        leaf = parsed.path.rstrip("/").split("/")[-1]
        return leaf or parsed.netloc
    return parsed.netloc


def _title_to_filename(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title or "")
    without_accents = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    upper = without_accents.upper()
    upper = re.sub(r"\bCOM\b", " ", upper)
    upper = re.sub(r"[^A-Z0-9]+", "_", upper)
    upper = re.sub(r"_+", "_", upper).strip("_")
    return upper[:120]


def _normalize_match_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    without_accents = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    lowered = without_accents.lower()
    return re.sub(r"[^a-z0-9]+", " ", lowered).strip()


_MODULE_HINTS_BY_FILENAME = [
    ("01 parametros e configuracao", "parametros_configuracao"),
    ("02 pedidos e vendas", "pedidos_vendas"),
    ("03 campanhas e descontos", "campanhas_descontos"),
    ("04 rotas visitas e consultas", "rotas_visitas_consultas"),
    ("05 sql banco e integracao", "sql_integracao"),
    ("layout integracao", "sql_integracao"),
    ("service desk", "suporte_processos"),
    ("glossario", "glossario"),
    ("tipos de venda", "pedidos_vendas"),
    ("maxpag", "financeiro_pagamentos"),
    ("base maxgestao", "gestao_operacional"),
]

_MODULE_HINTS_BY_KEYWORDS = {
    "sql_integracao": (
        " sql ",
        " tabela ",
        " select ",
        " endpoint ",
        " integracao ",
        " api ",
        " join ",
        " where ",
        " banco ",
    ),
    "parametros_configuracao": (
        " parametro ",
        " configuracao ",
        " permissao ",
        " central ",
        " perfil ",
        " sincronizacao ",
    ),
    "pedidos_vendas": (
        " pedido ",
        " venda ",
        " orcamento ",
        " pre pedido ",
        " cliente bloqueado ",
        " filial retira ",
        " timeline ",
    ),
    "campanhas_descontos": (
        " campanha ",
        " desconto ",
        " verba ",
        " miq ",
        " mqt ",
        " fpu ",
    ),
    "rotas_visitas_consultas": (
        " rota ",
        " visita ",
        " check in ",
        " check out ",
        " roteiro ",
    ),
    "financeiro_pagamentos": (
        " financeiro ",
        " pagamento ",
        " conta corrente ",
        " limite ",
        " inadimplente ",
    ),
}


def _infer_module(filename: str, title: str, source: str, doc_type: str) -> str:
    joined = _normalize_match_text(f"{filename} {title} {source} {doc_type}")
    padded = f" {joined} "

    for filename_hint, module in _MODULE_HINTS_BY_FILENAME:
        if filename_hint in joined:
            return module

    if doc_type.lower() == "sql":
        return "sql_integracao"

    for module, hints in _MODULE_HINTS_BY_KEYWORDS.items():
        if any(hint in padded for hint in hints):
            return module

    return "geral"


def _get_http_client() -> httpx.Client:
    global _http_client
    if _http_client is None:
        _http_client = httpx.Client(
            timeout=config.WEB_FETCH_TIMEOUT_SECONDS,
            follow_redirects=True,
            trust_env=False,
            headers={
                "User-Agent": config.WEB_USER_AGENT,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
                "Cache-Control": "no-cache",
            },
        )
    return _http_client


def _content_type_to_doc_type(content_type: str) -> str:
    ct = (content_type or "").lower()
    if "pdf" in ct:
        return "pdf"
    if "html" in ct:
        return "html"
    if "json" in ct:
        return "json"
    if "xml" in ct:
        return "xml"
    if "csv" in ct:
        return "csv"
    if "markdown" in ct:
        return "md"
    if "text/" in ct:
        return "txt"
    return "web"


def _clean_page_title(raw_title: str) -> str:
    title = re.sub(r"\s+", " ", (raw_title or "").strip())
    if not title:
        return ""
    for sep in (" - ", " | ", " — ", " – "):
        if sep in title:
            head = title.split(sep, 1)[0].strip()
            if len(head) >= 4:
                title = head
                break
    return title


def _html_to_text(html: str) -> tuple[str, str | None]:
    # Mantido para leitura de sites (HTML)
    page_title: str | None = None
    try:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, "html.parser")
        og_title = soup.find("meta", attrs={"property": "og:title"})
        if og_title and og_title.get("content"):
            page_title = str(og_title.get("content")).strip()
        if not page_title:
            h1 = soup.find("h1")
            if h1:
                page_title = h1.get_text(" ", strip=True)
        if not page_title and soup.title and soup.title.string:
            page_title = soup.title.string.strip()
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()
        text = soup.get_text("\n")
    except Exception:
        text = re.sub(r"<[^>]+>", " ", html)
        page_title = None

    lines = []
    for line in text.splitlines():
        clean = re.sub(r"\s+", " ", line).strip()
        if clean:
            lines.append(clean)
    return "\n".join(lines), _clean_page_title(page_title or "")


def _parse_zendesk_article_reference(url: str) -> tuple[str, str, str]:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 4 or parts[0].lower() != "hc" or parts[2].lower() != "articles":
        raise ValueError("URL nao parece ser artigo Zendesk")
    locale = parts[1]
    raw_article = parts[3]
    match = re.match(r"(\d+)", raw_article)
    if not match:
        raise ValueError("Nao foi possivel identificar article_id na URL")
    article_id = match.group(1)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    return base_url, locale, article_id


def _read_zendesk_article_api(url: str) -> tuple[str, str, str | None] | None:
    try:
        base_url, locale, article_id = _parse_zendesk_article_reference(url)
    except ValueError:
        return None
    api_urls = [
        f"{base_url}/api/v2/help_center/{locale}/articles/{article_id}.json",
        f"{base_url}/api/v2/help_center/articles/{article_id}.json",
    ]
    for api_url in api_urls:
        try:
            response = _get_http_client().get(api_url, headers={"Accept": "application/json"})
            response.raise_for_status()
            payload = response.json()
        except Exception:
            continue
        article = payload.get("article") if isinstance(payload, dict) else None
        if not isinstance(article, dict):
            continue
        title = _clean_page_title(str(article.get("title") or ""))
        body = str(article.get("body") or "")
        text, title_from_body = _html_to_text(body)
        if not title:
            title = title_from_body or _title_from_url(url)
        if text.strip():
            logger.info("URL %s lida via API Zendesk (%s)", url, api_url)
            return text, "html", title
    return None


def read_url(url: str) -> tuple[str, str, str | None]:
    if not _is_url(url):
        raise ValueError(f"URL invalida: {url}")
    if _is_private_url(url):
        raise ValueError(f"URL bloqueada por seguranca (IP privado/reservado): {url}")
    try:
        response = _get_http_client().get(url)
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        status_code = exc.response.status_code if exc.response is not None else None
        if status_code in {401, 403}:
            fallback = _read_zendesk_article_api(url)
            if fallback is not None:
                return fallback
        raise
    content_type = (response.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    lower_url = url.lower()
    page_title: str | None = None
    
    # Detecção se é PDF (URL ou Content-Type)
    if content_type == "application/pdf" or lower_url.endswith(".pdf"):
        text = read_pdf_bytes(response.content)
        doc_type = "pdf"
    else:
        doc_type = _content_type_to_doc_type(content_type)
        if doc_type == "html":
            text, page_title = _html_to_text(response.text)
        else:
            try:
                text = response.text
            except Exception:
                text = response.content.decode("utf-8", errors="ignore")

    if not text.strip():
        raise ValueError(f"Conteudo vazio na URL: {url}")

    max_chars = max(1000, config.WEB_MAX_TEXT_CHARS)
    if len(text) > max_chars:
        logger.warning("Conteudo de %s truncado para %s caracteres", url, max_chars)
        text = text[:max_chars]

    return text, doc_type, page_title


def _load_urls_from_file(filepath: str) -> list[str]:
    path = Path(filepath)
    if not path.exists():
        logger.warning("Arquivo de URLs nao encontrado: %s", path)
        return []
    urls: list[str] = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            candidates = re.findall(r"https?://[^\s)\]>\"']+", line)
            if not candidates and _is_url(line):
                candidates = [line]
            for url in candidates:
                if _is_url(url):
                    urls.append(url)
    return _dedupe_keep_order(urls)




# --- Contextual Retrieval (tecnica Anthropic) ---

_last_contextual_call_at = 0.0
_CONTEXTUAL_MIN_INTERVAL = 2.0  # segundos entre chamadas (evita 429)
_CONTEXTUAL_BATCH_SIZE = 10     # chunks por chamada LLM


def _wait_for_contextual_slot() -> None:
    """Rate limiting para chamadas ao Haiku — evita 429 Too Many Requests."""
    global _last_contextual_call_at
    now = time.monotonic()
    wait_for = (_last_contextual_call_at + _CONTEXTUAL_MIN_INTERVAL) - now
    if wait_for > 0:
        time.sleep(wait_for)
    _last_contextual_call_at = time.monotonic()


def _contextualize_chunks_batch(
    *,
    chunks_with_indices: list[tuple[int, str]],
    full_document: str,
    filename: str,
) -> list[tuple[int, str]]:
    """
    Contextual Retrieval em batch (Anthropic): envia varios chunks numa unica
    chamada ao LLM e recebe contextos para todos de uma vez.

    Reduz drasticamente o numero de chamadas API (ex: 120 chunks / 10 por batch = 12 chamadas).
    Em caso de erro, retorna os chunks originais (zero degradacao).

    Ref: https://www.anthropic.com/news/contextual-retrieval
    """
    if not config.CONTEXTUAL_RETRIEVAL_ENABLED or not chunks_with_indices:
        return chunks_with_indices

    truncated_doc = full_document[:config.CONTEXTUAL_RETRIEVAL_MAX_DOC_CHARS]

    # Montar a lista de chunks numerados no prompt
    chunks_section = ""
    for idx, (chunk_index, content) in enumerate(chunks_with_indices):
        chunks_section += f"<chunk id=\"{idx}\">\n{content}\n</chunk>\n\n"

    system_prompt = (
        "Voce e um assistente que situa trechos de documentos tecnicos no contexto geral "
        "do sistema maxPedido (Maxima Sistemas). "
        "Responda APENAS com um JSON array valido, sem explicacoes adicionais."
    )

    user_prompt = (
        f"<documento>\n{truncated_doc}\n</documento>\n\n"
        f"Abaixo estao {len(chunks_with_indices)} chunks extraidos deste documento:\n\n"
        f"{chunks_section}"
        "Para CADA chunk, forneca um contexto curto e sucinto (1-2 frases) que situe "
        "o chunk no documento geral, melhorando a busca por similaridade semantica. "
        "Inclua: de qual secao se trata, o tema principal, e termos tecnicos relevantes "
        "(nomes de tabelas, parametros, telas, modulos).\n\n"
        "Responda com um JSON array onde cada elemento e o contexto do chunk correspondente, "
        "na mesma ordem. Exemplo para 3 chunks:\n"
        '[\"contexto do chunk 0\", \"contexto do chunk 1\", \"contexto do chunk 2\"]\n\n'
        "JSON array:"
    )

    # max_tokens proporcional ao numero de chunks (~80 tokens por contexto)
    max_tokens = min(4096, len(chunks_with_indices) * 100)

    try:
        from rag import _gemini_generate

        _wait_for_contextual_slot()
        response = _gemini_generate(
            model=config.CONTEXTUAL_RETRIEVAL_MODEL,
            max_tokens=max_tokens,
            system=system_prompt,
            contents=user_prompt,
        )
        raw_text = response.text.strip()

        # Limpar markdown fences se o modelo envolver em ```json```
        if raw_text.startswith("```"):
            raw_text = re.sub(r"^```\w*\n?", "", raw_text)
            raw_text = re.sub(r"\n?```$", "", raw_text)

        contexts = json.loads(raw_text)

        if not isinstance(contexts, list) or len(contexts) != len(chunks_with_indices):
            logger.warning(
                "Contextual Retrieval batch para %s: esperava %d contextos, recebeu %d. Usando chunks originais.",
                filename, len(chunks_with_indices), len(contexts) if isinstance(contexts, list) else 0,
            )
            return chunks_with_indices

        # Aplicar contextos aos chunks
        result = []
        for (chunk_index, content), context in zip(chunks_with_indices, contexts):
            ctx = str(context).strip() if context else ""
            if ctx:
                result.append((chunk_index, f"{ctx}\n\n{content}"))
            else:
                result.append((chunk_index, content))

        logger.info(
            "Contextual Retrieval: %d chunks contextualizados para %s",
            len(result), filename,
        )
        return result

    except json.JSONDecodeError as e:
        logger.warning(
            "Contextual Retrieval batch para %s: JSON invalido: %s. Usando chunks originais.",
            filename, e,
        )
        return chunks_with_indices

    except Exception as e:
        logger.warning(
            "Contextual Retrieval batch para %s falhou: %s. Usando chunks originais.",
            filename, e,
        )
        return chunks_with_indices


def _ingest_text_source(
    *,
    filename: str,
    title: str,
    source: str,
    doc_type: str,
    text: str,
    source_type: str,
    force: bool,
) -> dict:
    if not text.strip():
        logger.warning("Fonte vazia: %s", filename)
        return {
            "filename": filename,
            "chunks_count": 0,
            "failed_chunks": 0,
            "error": "fonte vazia",
        }

    module = _infer_module(filename, title, source, doc_type)
    # P1.2: Usar chunking com headers contextuais
    chunks = chunk_text_with_context(text, doc_title=title)
    logger.info("%s chunks gerados para %s", len(chunks), filename)
    logger.info("Modulo inferido para %s: %s", filename, module)
    if config.CONTEXTUAL_RETRIEVAL_ENABLED:
        logger.info(
            "Contextual Retrieval ATIVO para %s (%d chunks serao enriquecidos via %s)",
            filename, len(chunks), config.CONTEXTUAL_RETRIEVAL_MODEL,
        )
    # P1.3: Inferir prioridade do documento
    doc_priority = _infer_priority(filename, chunk_count=len(chunks))

    existing = supabase_select("documents", select="id", filters={"filename": f"eq.{filename}"})

    if existing and force:
        temp_filename = f"__ingesting__{filename}"
        logger.info("Re-ingestao segura: inserindo %s com nome temporario", filename)
    elif existing and not force:
        logger.info("Pulando %s (ja indexado). Use --force para re-ingerir.", filename)
        return {
            "filename": filename,
            "chunks_count": 0,
            "failed_chunks": 0,
            "skipped": True,
        }
    else:
        temp_filename = None

    insert_filename = temp_filename if temp_filename else filename
    doc_result = supabase_insert(
        "documents",
        {
            "filename": insert_filename,
            "title": title,
            "source": source,
            "doc_type": doc_type,
            "chunk_count": 0,
        },
    )
    doc_id = doc_result[0]["id"]

    batch_size = max(1, config.EMBEDDING_BATCH_SIZE)
    total_inserted = 0
    failed_chunks: list[int] = []

    for batch_start in range(0, len(chunks), batch_size):
        batch = chunks[batch_start : batch_start + batch_size]
        clean_batch: list[tuple[int, str]] = []

        for i, chunk_text_content in enumerate(batch):
            chunk_index = batch_start + i
            clean_content = chunk_text_content.replace("\x00", "").strip()
            if not clean_content:
                failed_chunks.append(chunk_index)
                continue
            clean_batch.append((chunk_index, clean_content))

        # Contextual Retrieval em batch: enriquecer chunks com contexto do documento
        if clean_batch:
            for ctx_start in range(0, len(clean_batch), _CONTEXTUAL_BATCH_SIZE):
                ctx_sub = clean_batch[ctx_start : ctx_start + _CONTEXTUAL_BATCH_SIZE]
                ctx_result = _contextualize_chunks_batch(
                    chunks_with_indices=ctx_sub,
                    full_document=text,
                    filename=filename,
                )
                clean_batch[ctx_start : ctx_start + _CONTEXTUAL_BATCH_SIZE] = ctx_result

        if not clean_batch:
            continue

        rows = []
        indices = [item[0] for item in clean_batch]
        contents = [item[1] for item in clean_batch]

        try:
            embeddings = _embed_batch_with_retry(contents, filename, indices[0])
            for chunk_index, clean_content, embedding in zip(indices, contents, embeddings):
                rows.append(
                    {
                        "document_id": doc_id,
                        "content": clean_content,
                        "chunk_index": chunk_index,
                        "metadata": {
                            "filename": filename,
                            "chunk_index": chunk_index,
                            "doc_type": doc_type,
                            "source_type": source_type,
                            "module": module,
                            "title": title,
                            "doc_priority": doc_priority,
                        },
                        "embedding": embedding_to_pgvector(embedding),
                        "token_count": len(clean_content.split()),
                    }
                )
        except Exception as batch_error:
            logger.error(
                "Erro no lote de %s (chunk inicial %s): %s. Fallback chunk a chunk...",
                filename,
                batch_start,
                batch_error,
            )
            for chunk_index, clean_content in clean_batch:
                try:
                    embedding = _embed_batch_with_retry([clean_content], filename, chunk_index)[0]
                    rows.append(
                        {
                            "document_id": doc_id,
                            "content": clean_content,
                            "chunk_index": chunk_index,
                            "metadata": {
                                "filename": filename,
                                "chunk_index": chunk_index,
                                "doc_type": doc_type,
                                "source_type": source_type,
                                "module": module,
                                "title": title,
                                "doc_priority": doc_priority,
                            },
                            "embedding": embedding_to_pgvector(embedding),
                            "token_count": len(clean_content.split()),
                        }
                    )
                except Exception as chunk_error:
                    failed_chunks.append(chunk_index)
                    logger.error("Erro no chunk %s de %s: %s", chunk_index, filename, chunk_error)

        if rows:
            supabase_insert("document_chunks", rows)
            total_inserted += len(rows)

        logger.info("%s/%s chunks inseridos (%s)", total_inserted, len(chunks), filename)

    if temp_filename and existing:
        existing_doc_id = existing[0]["id"]
        try:
            supabase_delete("documents", "id", existing_doc_id)
            logger.info("Documento anterior removido: %s", filename)
        except Exception as e:
            logger.error("Erro ao remover documento anterior %s: %s", filename, e)

        supabase_update(
            "documents",
            {"filename": filename, "chunk_count": total_inserted},
            {"id": f"eq.{doc_id}"},
        )
    else:
        supabase_update("documents", {"chunk_count": total_inserted}, {"id": f"eq.{doc_id}"})

    _save_failed_report_entry(
        filename=filename,
        source=source,
        total_chunks=len(chunks),
        failed_chunks=failed_chunks,
        source_type=source_type,
    )

    if failed_chunks:
        logger.warning(
            "%s chunk(s) pendentes em %s. Relatorio: %s",
            len(failed_chunks),
            filename,
            config.FAILED_INGEST_REPORT,
        )
    else:
        logger.info("%s indexado sem pendencias", filename)

    return {
        "filename": filename,
        "chunks_count": total_inserted,
        "failed_chunks": len(failed_chunks),
        "module": module,
    }


def ingest_file(filepath: str, force: bool = False) -> dict:
    path = Path(filepath)
    ext = path.suffix.lower()

    if ext not in READERS:
        logger.warning("Formato nao suportado: %s (%s)", ext, path.name)
        return {
            "filename": path.name,
            "chunks_count": 0,
            "failed_chunks": 0,
            "error": "formato nao suportado",
        }

    logger.info("Lendo arquivo: %s", path.name)
    try:
        text = READERS[ext](filepath)
    except Exception as e:
        logger.error("Erro lendo %s: %s", path.name, e)
        return {"filename": path.name, "error": str(e)}

    if not text.strip():
        logger.warning("Arquivo vazio: %s", path.name)
        return {
            "filename": path.name,
            "chunks_count": 0,
            "failed_chunks": 0,
            "error": "arquivo vazio",
        }

    return _ingest_text_source(
        filename=path.name,
        title=path.stem,
        source=str(path.resolve()),
        doc_type=ext.lstrip("."),
        text=text,
        source_type="file",
        force=force,
    )


def ingest_url(url: str, force: bool = False) -> dict:
    logger.info("Lendo URL: %s", url)
    text, doc_type, page_title = read_url(url)

    filename = _url_to_filename(url)
    title = page_title or _title_from_url(url)

    return _ingest_text_source(
        filename=filename,
        title=title,
        source=url,
        doc_type=doc_type,
        text=text,
        source_type="url",
        force=force,
    )


def _collect_local_files(directory: str | None = None, create_if_missing: bool = False) -> tuple[Path, list[Path]]:
    docs_dir = directory if directory is not None else config.DOCS_DIR
    docs_path = Path(docs_dir)

    if not docs_path.exists():
        if create_if_missing:
            docs_path.mkdir(parents=True, exist_ok=True)
            logger.info("Diretorio criado: %s", docs_path)
            logger.info("Coloque seus documentos nele e execute novamente")
        return docs_path, []

    file_sources: list[Path] = []
    for ext in READERS:
        file_sources.extend(path for path in docs_path.glob(f"*{ext}") if path.is_file())

    deduped_sources: list[Path] = []
    seen: set[str] = set()
    for path in file_sources:
        key = str(path.resolve()).lower()
        if key in seen:
            continue
        seen.add(key)
        deduped_sources.append(path)

    return docs_path, deduped_sources

# --- Ingest Directory e Main mantidos similares ---

def ingest_directory(
    directory: str | None = None,
    retry_failed_only: bool = False,
    force: bool = False,
    urls: list[str] | None = None,
) -> list[dict]:
    file_sources: list[Path] = []
    url_sources = _dedupe_keep_order([u for u in (urls or []) if _is_url(u)])

    if retry_failed_only:
        failed_files, failed_urls = _failed_sources_from_report()
        file_sources = failed_files
        url_sources = _dedupe_keep_order(url_sources + failed_urls)
    else:
        docs_dir = directory if directory is not None else config.DOCS_DIR
        docs_path = Path(docs_dir)
        if not docs_path.exists():
            docs_path.mkdir(parents=True, exist_ok=True)
            return []
        _, file_sources = _collect_local_files(directory=directory, create_if_missing=False)

    if not force and not retry_failed_only:
        indexed = _get_indexed_filenames()
        file_sources = [f for f in file_sources if f.name not in indexed]
        url_sources = [u for u in url_sources if _url_to_filename(u) not in indexed]

    results = []
    for filepath in sorted(file_sources):
        try:
            results.append(ingest_file(str(filepath), force=force))
        except Exception as exc:
            logger.error("Erro ao processar %s: %s", filepath.name, exc)

    for url in url_sources:
        try:
            results.append(ingest_url(url, force=force))
        except Exception as exc:
            logger.error("Erro URL %s: %s", url, exc)

    return results


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingestao de documentos e URLs para RAG")
    parser.add_argument("directory", nargs="?", default=None, help="Diretorio de documentos")
    parser.add_argument("--force", action="store_true", help="Re-ingere fontes ja indexadas")
    parser.add_argument("--retry-failed", action="store_true")
    parser.add_argument("--url", action="append", default=[])
    parser.add_argument("--urls-file", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()

    urls = list(args.url or [])
    if args.urls_file:
        urls.extend(_load_urls_from_file(args.urls_file))

    ingest_directory(
        directory=args.directory,
        retry_failed_only=args.retry_failed,
        force=args.force,
        urls=urls,
    )
