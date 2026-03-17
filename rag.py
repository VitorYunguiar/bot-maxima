"""
rag.py — Pipeline RAG: embedding (Gemini) → busca hibrida (Supabase REST) → resposta (Gemini)
Usa HTTP direto com Supabase para evitar dependencias pesadas.
Suporta busca hibrida (vetor + full-text) com Reciprocal Rank Fusion.
"""

import atexit
import base64 as _base64
import logging
import math
import random as _random
import re
import time as _time
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
import unicodedata

import httpx
from google import genai
from google.genai import types as _gtypes

import config

logger = logging.getLogger(__name__)

_knowledge_gap_rpc_available: Optional[bool] = None
_top_knowledge_gaps_rpc_available: Optional[bool] = None
_business_rules_cache: Optional[tuple[str, float, str]] = None
_full_context_cache: Optional[tuple[str, float]] = None  # (text, mtime_max)

# Expansao de abreviaturas do dominio para embedding de query.
# Mantem a query original para FTS.
# Ajuste os valores abaixo conforme o glossario interno da operacao.
QUERY_ABBREVIATIONS = {
    "RCA": "representante comercial autonomo",
    "NF": "nota fiscal",
    "NFE": "nota fiscal eletronica",
    "FPU": "F P U",
    "MIQ": "M I Q",
    "MQT": "M Q T",
    "PDV": "ponto de venda",
    "SKU": "stock keeping unit",
    "WMS": "warehouse management system",
}

INTENT_PRIORITY = [
    "sql_lookup",
    "troubleshooting",
    "integration",
    "configuration",
    "process",
    "general",
]

INTENT_KEYWORDS = {
    "sql_lookup": (
        "sql",
        "select",
        "from",
        "join",
        "where",
        "tabela",
        "campo",
        "coluna",
        "query",
        "banco",
    ),
    "configuration": (
        "parametro",
        "configuracao",
        "permissao",
        "habilitar",
        "desabilitar",
        "central",
        "perfil",
        "sincronizacao",
    ),
    "integration": (
        "integracao",
        "endpoint",
        "api",
        "erp",
        "statuspedidos",
        "mixintegracaopedido",
        "mxshistoricopedc",
        "webhook",
    ),
    "troubleshooting": (
        "erro",
        "falha",
        "nao funciona",
        "nao atualiza",
        "travou",
        "critica",
        "problema",
        "corrigir",
        "ajuda",
    ),
    "process": (
        "pedido",
        "venda",
        "orcamento",
        "pre pedido",
        "filial retira",
        "cliente bloqueado",
        "timeline",
        "roteiro",
        "visita",
    ),
}

QUERY_MODULE_HINTS = {
    "sql_integracao": (
        "sql",
        "select",
        "join",
        "where",
        "tabela",
        "campo",
        "coluna",
        "integracao",
        "endpoint",
        "api",
        "erp",
    ),
    "parametros_configuracao": (
        "parametro",
        "configuracao",
        "permissao",
        "central",
        "sincronizacao",
        "perfil",
    ),
    "pedidos_vendas": (
        "pedido",
        "venda",
        "orcamento",
        "cliente bloqueado",
        "filial retira",
        "pre pedido",
        "timeline",
    ),
    "campanhas_descontos": (
        "campanha",
        "desconto",
        "miq",
        "mqt",
        "fpu",
        "sqp",
    ),
    "rotas_visitas_consultas": (
        "rota",
        "roteiro",
        "visita",
        "check in",
        "check out",
    ),
    "financeiro_pagamentos": (
        "financeiro",
        "pagamento",
        "inadimplente",
        "limite",
        "conta corrente",
    ),
}

INTENT_DEFAULT_MODULES = {
    "sql_lookup": ["sql_integracao"],
    "integration": ["sql_integracao", "suporte_processos"],
    "configuration": ["parametros_configuracao"],
    "process": ["pedidos_vendas"],
    "troubleshooting": ["suporte_processos", "pedidos_vendas"],
}

INTENT_DOC_TYPES = {
    "sql_lookup": ["md", "pdf", "txt"],
    "integration": ["md", "pdf", "txt", "json"],
    "configuration": ["md", "pdf", "txt"],
    "process": ["md", "pdf", "txt"],
    "troubleshooting": ["md", "pdf", "txt"],
}

INTENT_RESPONSE_INSTRUCTIONS = {
    "sql_lookup": (
        "Para perguntas SQL/tabela, estruture a resposta em: "
        "objetivo, tabelas principais, campos-chave e validacao. "
        "Inclua SQL somente se estiver no contexto."
    ),
    "configuration": (
        "Para configuracoes, traga caminho exato (menu/tela/campo) quando houver, "
        "parametros envolvidos e impacto esperado."
    ),
    "integration": (
        "Para integracao, destaque fluxo origem-destino, tabelas/enderecos envolvidos "
        "e pontos de validacao operacional."
    ),
    "troubleshooting": (
        "Para troubleshooting, responda com checklist objetivo: "
        "causa provavel, verificacoes e acao recomendada."
    ),
    "process": (
        "Para processo de negocio, responda passo a passo curto e com pre-condicoes."
    ),
}

# ── Clientes ──────────────────────────────────────────────
_gemini: Optional[genai.Client] = None
_http_client: Optional[httpx.Client] = None


def get_gemini() -> genai.Client:
    global _gemini
    if _gemini is None:
        _gemini = genai.Client(api_key=config.GEMINI_API_KEY)
    return _gemini


def _gemini_generate(
    model: str,
    *,
    system: str | None = None,
    contents,
    max_tokens: int = 2048,
):
    """Wrapper para chamadas ao Gemini que padroniza config."""
    cfg = _gtypes.GenerateContentConfig(max_output_tokens=max_tokens)
    if system:
        cfg.system_instruction = system
    response = get_gemini().models.generate_content(
        model=model,
        contents=contents,
        config=cfg,
    )
    return response


def _anthropic_msgs_to_gemini(messages: list[dict]) -> list[_gtypes.Content]:
    """Converte historico no formato Anthropic (role/content) para Gemini Content."""
    result = []
    for msg in messages:
        role = "model" if msg["role"] == "assistant" else "user"
        content = msg.get("content", "")
        if isinstance(content, str):
            parts = [_gtypes.Part(text=content)]
        elif isinstance(content, list):
            parts = []
            for block in content:
                if isinstance(block, str):
                    parts.append(_gtypes.Part(text=block))
                elif isinstance(block, dict):
                    if block.get("type") == "text":
                        parts.append(_gtypes.Part(text=block["text"]))
                    elif block.get("type") == "image":
                        src = block["source"]
                        parts.append(_gtypes.Part(
                            inline_data=_gtypes.Blob(
                                mime_type=src["media_type"],
                                data=_base64.b64decode(src["data"]),
                            )
                        ))
        else:
            parts = [_gtypes.Part(text=str(content))]
        result.append(_gtypes.Content(role=role, parts=parts))
    return result


def _get_http_client() -> httpx.Client:
    """Retorna httpx.Client reutilizavel com connection pooling."""
    global _http_client
    if _http_client is None:
        _http_client = httpx.Client(
            timeout=60,
            trust_env=False,
            limits=httpx.Limits(max_connections=10, max_keepalive_connections=5),
        )
        atexit.register(_close_http_client)
    return _http_client


def _close_http_client():
    """Fecha o httpx client no shutdown do processo."""
    global _http_client
    if _http_client is not None:
        try:
            _http_client.close()
        except Exception:
            logger.debug("Erro ao fechar http client no shutdown", exc_info=True)
        _http_client = None


def _supabase_headers() -> dict:
    return {
        "apikey": config.SUPABASE_SERVICE_KEY,
        "Authorization": f"Bearer {config.SUPABASE_SERVICE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


def _supabase_url(path: str) -> str:
    return f"{config.SUPABASE_URL}/rest/v1/{path}"


# ── Retry para erros transientes ─────────────────────────
def _retry_on_transient(fn, max_retries: int = 2, backoff: float = 1.0):
    """Retenta chamadas HTTP em erros transientes (429, 502, 503, 504) com backoff exponencial."""
    for attempt in range(max_retries + 1):
        try:
            return fn()
        except httpx.HTTPStatusError as e:
            if e.response.status_code in (429, 502, 503, 504) and attempt < max_retries:
                delay = backoff * (2 ** attempt) + _random.uniform(0, 1.0)
                logger.warning(
                    "Erro transiente %s, tentativa %s/%s. Aguardando %.1fs...",
                    e.response.status_code,
                    attempt + 1,
                    max_retries,
                    delay,
                )
                _time.sleep(delay)
                continue
            raise


# ── Supabase REST helpers ─────────────────────────────────
def supabase_insert(table: str, data: dict | list) -> list:
    """Insere dados via REST API do Supabase."""
    def _do():
        resp = _get_http_client().post(
            _supabase_url(table),
            headers=_supabase_headers(),
            json=data,
            timeout=120,  # insercoes de lotes podem demorar
        )
        if resp.status_code >= 400:
            logger.error(
                "Supabase INSERT erro %s em %s: %s",
                resp.status_code,
                table,
                resp.text[:2000],
            )
        resp.raise_for_status()
        return resp.json()
    return _retry_on_transient(_do)


def supabase_select(table: str, select: str = "*", filters: dict = None) -> list:
    params = {"select": select}
    if filters:
        for key, value in filters.items():
            params[key] = value

    def _do():
        resp = _get_http_client().get(
            _supabase_url(table),
            headers=_supabase_headers(),
            params=params,
        )
        if resp.status_code >= 400:
            logger.error(
                "Supabase SELECT erro %s em %s: %s",
                resp.status_code,
                table,
                resp.text[:2000],
            )
        resp.raise_for_status()
        return resp.json()
    return _retry_on_transient(_do)


def supabase_delete(table: str, column: str, value: str) -> None:
    def _do():
        resp = _get_http_client().delete(
            _supabase_url(table),
            headers=_supabase_headers(),
            params={column: f"eq.{value}"},
        )
        if resp.status_code >= 400:
            logger.error(
                "Supabase DELETE erro %s em %s.%s=%s: %s",
                resp.status_code,
                table,
                column,
                value,
                resp.text[:2000],
            )
        resp.raise_for_status()
    _retry_on_transient(_do)


def supabase_update(table: str, data: dict, filters: dict) -> list:
    params = {}
    for key, value in filters.items():
        params[key] = value

    def _do():
        resp = _get_http_client().patch(
            _supabase_url(table),
            headers=_supabase_headers(),
            params=params,
            json=data,
        )
        if resp.status_code >= 400:
            logger.error(
                "Supabase UPDATE erro %s em %s: %s",
                resp.status_code,
                table,
                resp.text[:2000],
            )
        resp.raise_for_status()
        return resp.json()
    return _retry_on_transient(_do)


def supabase_rpc(function_name: str, params: dict) -> list:
    def _do():
        resp = _get_http_client().post(
            f"{config.SUPABASE_URL}/rest/v1/rpc/{function_name}",
            headers=_supabase_headers(),
            json=params,
        )
        if resp.status_code >= 400:
            logger.error(
                "Supabase RPC erro %s em %s: %s",
                resp.status_code,
                function_name,
                resp.text[:2000],
            )
        resp.raise_for_status()
        # Funcoes SQL RETURNS VOID podem responder 204 sem corpo.
        if resp.status_code == 204 or not resp.content:
            return []
        try:
            return resp.json()
        except ValueError:
            # Evita quebrar o fluxo quando PostgREST devolve sucesso sem JSON valido.
            logger.warning(
                "Supabase RPC respondeu sem JSON valido em %s (status=%s).",
                function_name,
                resp.status_code,
            )
            return []
    return _retry_on_transient(_do)


def _is_missing_rpc_function(error: Exception, function_name: str) -> bool:
    if not isinstance(error, httpx.HTTPStatusError):
        return False
    response = error.response
    if response is None or response.status_code != 404:
        return False
    body = response.text or ""
    return "PGRST202" in body or function_name in body


def _safe_similarity(value: float) -> float:
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return 0.0
    if not math.isfinite(parsed):
        return 0.0
    return parsed


def _fallback_log_knowledge_gap(query: str, max_similarity: float, platform: str) -> None:
    normalized_query = query[:500]
    similarity = _safe_similarity(max_similarity)

    rows = supabase_select(
        "knowledge_gaps",
        select="id,occurrences,max_similarity",
        filters={
            "query": f"eq.{normalized_query}",
            "limit": 1,
        },
    )

    if rows:
        row = rows[0]
        row_id = row.get("id")
        if row_id:
            now_iso = datetime.now(timezone.utc).isoformat()
            supabase_update(
                "knowledge_gaps",
                {
                    "occurrences": int(row.get("occurrences", 0) or 0) + 1,
                    "max_similarity": max(
                        _safe_similarity(row.get("max_similarity", 0.0)),
                        similarity,
                    ),
                    "platform": platform,
                    "last_seen": now_iso,
                },
                {"id": f"eq.{row_id}"},
            )
            return

    supabase_insert(
        "knowledge_gaps",
        {
            "query": normalized_query,
            "max_similarity": similarity,
            "platform": platform,
            "occurrences": 1,
        },
    )


def _fallback_get_top_knowledge_gaps(limit: int) -> list[dict]:
    safe_limit = max(1, min(int(limit), 100))
    return supabase_select(
        "knowledge_gaps",
        select="query,occurrences,max_similarity,platform,last_seen",
        filters={
            "resolved": "eq.false",
            "order": "occurrences.desc,last_seen.desc",
            "limit": safe_limit,
        },
    )


# ── Embedding (Google Gemini - GRATIS) ────────────────────
def _normalize_embedding(values: list[float]) -> list[float]:
    values = [v if math.isfinite(v) else 0.0 for v in values]
    target_dims = config.EMBEDDING_DIMENSIONS
    if len(values) > target_dims:
        logger.warning(
            "Embedding maior que o esperado (%s > %s); truncando.",
            len(values),
            target_dims,
        )
        values = values[:target_dims]
    elif len(values) < target_dims:
        logger.warning(
            "Embedding menor que o esperado (%s < %s); preenchendo com zeros.",
            len(values),
            target_dims,
        )
        values.extend([0.0] * (target_dims - len(values)))
    return values


def create_embeddings(contents: list[str], task_type: str = "RETRIEVAL_DOCUMENT") -> list[list[float]]:
    if not contents:
        return []

    payload = contents if len(contents) > 1 else contents[0]
    result = get_gemini().models.embed_content(
        model=config.EMBEDDING_MODEL,
        contents=payload,
        config={
            "task_type": task_type,
            "output_dimensionality": config.EMBEDDING_DIMENSIONS,
        },
    )

    embeddings = getattr(result, "embeddings", None) or []
    if not embeddings and len(contents) == 1:
        single_embedding = getattr(result, "embedding", None)
        if single_embedding is not None:
            embeddings = [single_embedding]
    vectors = [_normalize_embedding([float(v) for v in emb.values]) for emb in embeddings]
    if len(vectors) != len(contents):
        raise ValueError(
            f"Quantidade de embeddings inconsistente: esperado {len(contents)}, obtido {len(vectors)}."
        )
    return vectors


def create_embedding(text: str, task_type: str = "RETRIEVAL_DOCUMENT") -> list[float]:
    return create_embeddings([text], task_type=task_type)[0]


def create_query_embedding(text: str) -> list[float]:
    return create_embedding(text, task_type="RETRIEVAL_QUERY")


def create_document_embedding(text: str) -> list[float]:
    return create_embedding(text, task_type="RETRIEVAL_DOCUMENT")


def create_document_embeddings(texts: list[str]) -> list[list[float]]:
    return create_embeddings(texts, task_type="RETRIEVAL_DOCUMENT")


def embedding_to_pgvector(embedding: list[float]) -> str:
    """
    Converte lista de floats para o formato string que o pgvector aceita via PostgREST.
    Formato: '[0.1,0.2,0.3,...]'
    Sanitiza valores NaN/Inf para 0.0.
    """
    sanitized = [v if math.isfinite(v) else 0.0 for v in embedding]
    return "[" + ",".join(str(v) for v in sanitized) + "]"


# ── Cache de query embeddings (LRU com TTL) ──────────────
class _TTLCache:
    """Cache LRU com TTL. Evicao O(1) via OrderedDict."""

    def __init__(self, maxsize: int = 500, ttl: float = 3600.0):
        self._cache: OrderedDict[str, tuple[list[float], float]] = OrderedDict()
        self._maxsize = maxsize
        self._ttl = ttl

    def get(self, key: str) -> list[float] | None:
        entry = self._cache.get(key)
        if entry is None:
            return None
        value, ts = entry
        if (_time.monotonic() - ts) >= self._ttl:
            del self._cache[key]
            return None
        self._cache.move_to_end(key)
        return value

    def put(self, key: str, value: list[float]) -> None:
        self._cache[key] = (value, _time.monotonic())
        self._cache.move_to_end(key)
        while len(self._cache) > self._maxsize:
            self._cache.popitem(last=False)  # O(1) — remove o mais antigo


_query_embedding_cache = _TTLCache(maxsize=500, ttl=3600.0)


def _get_cached_query_embedding(query: str) -> list[float]:
    """Retorna embedding de query com cache in-memory (TTL 1h, LRU)."""
    cached = _query_embedding_cache.get(query)
    if cached is not None:
        logger.debug("Cache hit para query embedding: '%s'", query[:60])
        return cached

    embedding = create_query_embedding(query)
    _query_embedding_cache.put(query, embedding)
    return embedding


def _preprocess_query(query: str) -> tuple[str, str]:
    """Retorna (query_para_embedding, query_para_fts)."""
    query_for_fts = query
    query_for_embedding = query

    for abbreviation, expansion in QUERY_ABBREVIATIONS.items():
        pattern = rf"\b{re.escape(abbreviation)}\b"
        query_for_embedding = re.sub(
            pattern,
            lambda m: f"{m.group(0)} {expansion}",
            query_for_embedding,
            flags=re.IGNORECASE,
        )

    query_for_embedding = re.sub(r"\s+", " ", query_for_embedding).strip() or query
    return query_for_embedding, query_for_fts


def _normalize_route_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    without_accents = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    lowered = without_accents.lower()
    compact = re.sub(r"[^a-z0-9]+", " ", lowered).strip()
    return f" {compact} "


def _classify_query_intent(query: str) -> dict:
    if not config.RAG_ENABLE_INTENT_ROUTING:
        return {"intent": "general", "doc_types": [], "modules": []}

    normalized = _normalize_route_text(query)
    scores: dict[str, int] = {}

    for intent, keywords in INTENT_KEYWORDS.items():
        score = 0
        for keyword in keywords:
            normalized_keyword = _normalize_route_text(keyword).strip()
            if f" {normalized_keyword} " in normalized:
                score += 1
        if score > 0:
            scores[intent] = score

    if scores:
        best_score = max(scores.values())
        tied = {intent for intent, score in scores.items() if score == best_score}
        intent = next((candidate for candidate in INTENT_PRIORITY if candidate in tied), "general")
    else:
        intent = "general"

    modules: set[str] = set(INTENT_DEFAULT_MODULES.get(intent, []))
    for module, keywords in QUERY_MODULE_HINTS.items():
        for keyword in keywords:
            normalized_keyword = _normalize_route_text(keyword).strip()
            if f" {normalized_keyword} " in normalized:
                modules.add(module)
                break

    doc_types = list(INTENT_DOC_TYPES.get(intent, []))
    return {
        "intent": intent,
        "doc_types": doc_types,
        "modules": sorted(modules),
    }


def _build_search_filters(query_plan: dict | None) -> tuple[list[str] | None, list[str] | None]:
    if not query_plan:
        return None, None

    doc_types = query_plan.get("doc_types") if config.RAG_FILTER_BY_DOC_TYPE else None
    modules = query_plan.get("modules") if config.RAG_FILTER_BY_MODULE else None

    normalized_doc_types = [str(v).lower() for v in (doc_types or []) if str(v).strip()]
    normalized_modules = [str(v).lower() for v in (modules or []) if str(v).strip()]

    return normalized_doc_types or None, normalized_modules or None


def _search_rpc_with_filter_fallback(function_name: str, params: dict) -> list:
    try:
        return _retry_on_transient(lambda: supabase_rpc(function_name, params))
    except Exception as e:
        has_filters = "filter_doc_types" in params or "filter_modules" in params
        if has_filters and _is_missing_rpc_function(e, function_name):
            fallback_params = {
                key: value
                for key, value in params.items()
                if key not in {"filter_doc_types", "filter_modules"}
            }
            logger.warning(
                "Supabase ainda sem suporte a filtros opcionais em %s; repetindo sem filtros.",
                function_name,
            )
            return _retry_on_transient(lambda: supabase_rpc(function_name, fallback_params))
        raise


def _load_business_rules_context() -> str:
    if not config.RAG_ENABLE_BUSINESS_RULES:
        return ""

    rules_path = Path(config.BUSINESS_RULES_FILE)
    if not rules_path.exists() or not rules_path.is_file():
        return ""

    resolved_path = str(rules_path.resolve())
    mtime = rules_path.stat().st_mtime
    global _business_rules_cache

    if _business_rules_cache:
        cached_path, cached_mtime, cached_text = _business_rules_cache
        if cached_path == resolved_path and cached_mtime == mtime:
            return cached_text

    text = rules_path.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return ""

    max_chars = max(500, int(config.BUSINESS_RULES_MAX_CHARS))
    if len(text) > max_chars:
        logger.warning(
            "Arquivo de regras de negocio excede limite (%s chars). Truncando para %s.",
            len(text),
            max_chars,
        )
        text = text[:max_chars]

    _business_rules_cache = (resolved_path, mtime, text)
    return text


def _load_full_context_docs() -> str:
    """Carrega todos os documentos do diretorio raiz como contexto completo (estilo Claude Projects).

    Retorna o texto concatenado de todos os documentos, com marcadores de documento.
    Usa cache em memoria e recarrega somente se algum arquivo mudou.
    """
    if not config.FULL_CONTEXT_ENABLED:
        return ""

    global _full_context_cache
    docs_dir = Path(config.DOCS_DIR)
    if not docs_dir.exists() or not docs_dir.is_dir():
        logger.warning("FULL_CONTEXT: Diretorio de documentos nao encontrado: %s", docs_dir)
        return ""

    allowed_exts = {ext.strip().lower() for ext in config.FULL_CONTEXT_EXTENSIONS}
    doc_files = sorted(
        f for f in docs_dir.iterdir()
        if f.is_file() and f.suffix.lower() in allowed_exts
    )

    if not doc_files:
        logger.warning("FULL_CONTEXT: Nenhum documento encontrado em %s", docs_dir)
        return ""

    current_mtime_max = max(f.stat().st_mtime for f in doc_files)
    if _full_context_cache:
        cached_text, cached_mtime = _full_context_cache
        if cached_mtime == current_mtime_max:
            return cached_text

    parts: list[str] = []
    total_chars = 0
    max_chars = config.FULL_CONTEXT_MAX_CHARS

    for doc_file in doc_files:
        try:
            content = doc_file.read_text(encoding="utf-8", errors="ignore").strip()
        except Exception as e:
            logger.warning("FULL_CONTEXT: Erro ao ler %s: %s", doc_file.name, e)
            continue

        if not content:
            continue

        if total_chars + len(content) > max_chars:
            remaining = max_chars - total_chars
            if remaining > 1000:
                content = content[:remaining]
                logger.warning(
                    "FULL_CONTEXT: Documento %s truncado para caber no limite.", doc_file.name
                )
            else:
                logger.warning(
                    "FULL_CONTEXT: Limite de %d chars atingido. %s ignorado.",
                    max_chars, doc_file.name,
                )
                break

        parts.append(
            f"<document source=\"{doc_file.name}\">\n"
            f"{content}\n"
            f"</document>"
        )
        total_chars += len(content)

    full_text = "\n\n".join(parts)
    _full_context_cache = (full_text, current_mtime_max)
    logger.info(
        "FULL_CONTEXT: %d documentos carregados (%d chars total).",
        len(parts), total_chars,
    )
    return full_text


def _intent_response_instruction(query_plan: dict | None) -> str:
    if not query_plan:
        return ""
    intent = str(query_plan.get("intent") or "general")
    return INTENT_RESPONSE_INSTRUCTIONS.get(intent, "")


def _postprocess_search_results(
    chunks: list[dict],
    max_results: int,
    threshold: float,
) -> list[dict]:
    if not chunks:
        return []

    min_similarity = threshold * config.SIMILARITY_FLOOR_FACTOR
    filtered = [
        c for c in chunks
        if _safe_similarity(c.get("similarity", 0)) >= min_similarity
    ]

    filtered.sort(
        key=lambda c: _safe_similarity(c.get("similarity", 0)),
        reverse=True,
    )

    max_with_neighbors = max(1, max_results * 2)
    if len(filtered) > max_with_neighbors:
        filtered = filtered[:max_with_neighbors]

    return filtered


# ── Busca semantica (hibrida: vetor + full-text) ─────────
def search_similar_chunks(
    query: str,
    max_results: int = None,
    threshold: float = None,
    query_plan: dict | None = None,
) -> list[dict]:
    if max_results is None:
        max_results = config.MAX_CONTEXT_CHUNKS
    if threshold is None:
        threshold = config.SIMILARITY_THRESHOLD

    query_for_embedding, query_for_fts = _preprocess_query(query)
    query_embedding = _get_cached_query_embedding(query_for_embedding)
    doc_types_filter, module_filter = _build_search_filters(query_plan)
    rpc_params = {
        "query_embedding": embedding_to_pgvector(query_embedding),
        "query_text": query_for_fts,
        "match_count": max_results,
        "match_threshold": threshold,
    }
    if doc_types_filter:
        rpc_params["filter_doc_types"] = doc_types_filter
    if module_filter:
        rpc_params["filter_modules"] = module_filter

    if query_plan and (doc_types_filter or module_filter):
        logger.info(
            "Roteamento de busca: intent=%s doc_types=%s modules=%s",
            query_plan.get("intent", "general"),
            doc_types_filter or [],
            module_filter or [],
        )

    # Tentar busca hibrida primeiro (vetor + full-text com RRF)
    try:
        result = _search_rpc_with_filter_fallback(
            "hybrid_match_chunks",
            rpc_params,
        )
        if result:
            result = _postprocess_search_results(result, max_results, threshold)
        if result:
            logger.info(
                "Busca hibrida: %d chunks encontrados para '%s'",
                len(result),
                query[:80],
            )
            return result
        logger.info(
            "Busca hibrida sem chunks acima do piso minimo para '%s'",
            query[:80],
        )
    except Exception as e:
        logger.warning(
            "Busca hibrida falhou (%s), usando busca vetorial pura.", e
        )

    # Fallback: busca vetorial pura (match_chunks original)
    vector_params = {
        "query_embedding": rpc_params["query_embedding"],
        "match_count": max_results,
        "match_threshold": threshold,
    }
    if doc_types_filter:
        vector_params["filter_doc_types"] = doc_types_filter
    if module_filter:
        vector_params["filter_modules"] = module_filter

    result = _search_rpc_with_filter_fallback(
        "match_chunks",
        vector_params,
    )
    if result:
        result = _postprocess_search_results(result, max_results, threshold)

    if result:
        logger.info(
            "Busca vetorial pura: %d chunks encontrados para '%s'",
            len(result),
            query[:80],
        )
    else:
        logger.warning(
            "Nenhum chunk encontrado para '%s' (threshold=%.2f)",
            query[:80],
            threshold,
        )

    final_result = result or []

    # P0.3: Se a busca filtrada retornou poucos resultados, complementar sem filtro de modulo
    if module_filter and len(final_result) < max(1, max_results // 2):
        logger.info(
            "Busca filtrada retornou poucos resultados (%d/%d); "
            "complementando com busca sem filtro de modulo.",
            len(final_result),
            max_results,
        )
        found_ids = {c.get("id") for c in final_result}
        unfiltered_params = {
            "query_embedding": rpc_params["query_embedding"],
            "query_text": query_for_fts,
            "match_count": max_results,
            "match_threshold": threshold,
        }
        if doc_types_filter:
            unfiltered_params["filter_doc_types"] = doc_types_filter
        try:
            extra = _search_rpc_with_filter_fallback("hybrid_match_chunks", unfiltered_params)
            if extra:
                extra = _postprocess_search_results(extra, max_results, threshold)
                for chunk in extra:
                    if chunk.get("id") not in found_ids:
                        final_result.append(chunk)
                        found_ids.add(chunk.get("id"))
                final_result.sort(
                    key=lambda c: _safe_similarity(c.get("similarity", 0)),
                    reverse=True,
                )
                max_with_neighbors = max(1, max_results * 2)
                if len(final_result) > max_with_neighbors:
                    final_result = final_result[:max_with_neighbors]
                logger.info(
                    "Busca complementar sem filtro de modulo: %d chunks total apos merge.",
                    len(final_result),
                )
        except Exception as e:
            logger.warning("Busca complementar sem filtro de modulo falhou: %s", e)

    return final_result


def _chunk_index_value(chunk: dict) -> int:
    try:
        return int(chunk.get("chunk_index", 0))
    except (TypeError, ValueError):
        return 0


def _trim_chunk_overlap(previous_text: str, current_text: str, max_overlap: int) -> str:
    if not previous_text or not current_text or max_overlap <= 0:
        return current_text

    max_window = min(max_overlap, len(previous_text), len(current_text))
    min_overlap = 40
    if max_window < min_overlap:
        return current_text
    for overlap_size in range(max_window, min_overlap - 1, -1):
        if previous_text[-overlap_size:] == current_text[:overlap_size]:
            return current_text[overlap_size:].lstrip()
    return current_text


def _merge_document_chunks(doc_chunks: list[dict]) -> str:
    parts: list[str] = []
    previous_content = ""
    previous_chunk_index: int | None = None

    for chunk in doc_chunks:
        content = chunk.get("content", "") or ""
        if not content.strip():
            continue

        chunk_index = _chunk_index_value(chunk)
        merged_content = content
        if previous_chunk_index is not None and chunk_index == previous_chunk_index + 1:
            merged_content = _trim_chunk_overlap(
                previous_content,
                content,
                config.CHUNK_OVERLAP,
            )

        if merged_content.strip():
            parts.append(merged_content)

        previous_content = content
        previous_chunk_index = chunk_index

    return "\n\n".join(parts)


# -- Montagem do contexto -------------------------------------------------------
def build_context(chunks: list[dict]) -> str:
    if not chunks:
        return ""

    chunks_by_doc: dict[str, list[dict]] = {}
    for chunk in chunks:
        doc_key = str(chunk.get("document_id") or chunk.get("filename") or "desconhecido")
        chunks_by_doc.setdefault(doc_key, []).append(chunk)

    docs_for_context: list[dict] = []
    for doc_chunks in chunks_by_doc.values():
        sorted_doc_chunks = sorted(doc_chunks, key=_chunk_index_value)
        merged_content = _merge_document_chunks(sorted_doc_chunks)
        if not merged_content.strip():
            continue

        filename = next(
            (c.get("filename") for c in sorted_doc_chunks if c.get("filename")),
            "desconhecido",
        )
        max_similarity = max(
            _safe_similarity(c.get("similarity", 0))
            for c in sorted_doc_chunks
        )

        # P1.3: Boost de prioridade do documento
        doc_priority = 5  # default
        for c in sorted_doc_chunks:
            meta = c.get("metadata") or {}
            if isinstance(meta, dict):
                p = meta.get("doc_priority")
                if p is not None:
                    try:
                        doc_priority = int(p)
                    except (TypeError, ValueError):
                        pass
                    break

        # Boost sutil: priority 10 → +10%, priority 3 → -4%
        priority_boost = 1.0 + (doc_priority - 5) * 0.02
        sort_similarity = max_similarity * priority_boost

        docs_for_context.append(
            {
                "filename": filename,
                "max_similarity": max_similarity,
                "sort_similarity": sort_similarity,
                "merged_content": merged_content,
                "chunk_count": len(sorted_doc_chunks),
            }
        )

    docs_for_context.sort(key=lambda d: (-d["sort_similarity"], d["filename"]))

    context_parts = []
    for index, doc in enumerate(docs_for_context, start=1):
        context_parts.append(
            f"<document index=\"{index}\" source=\"{doc['filename']}\" relevance=\"{doc['max_similarity']:.2f}\" chunks=\"{doc['chunk_count']}\">\n"
            f"{doc['merged_content']}\n"
            f"</document>"
        )

    return "\n\n".join(context_parts)


# -- Reformulacao de query com historico (P0.1) ---------------------------------
def _reformulate_query_with_history(
    question: str,
    conversation_history: list[dict] | None,
) -> str:
    """Usa historico recente para tornar perguntas de follow-up autocontidas."""
    if not config.RAG_ENABLE_QUERY_REFORMULATION:
        return question
    if not conversation_history:
        return question

    # Perguntas com 6+ palavras provavelmente ja sao autocontidas
    if len(question.split()) >= 6:
        return question

    # Usar apenas os ultimos 2 pares (4 mensagens)
    recent = conversation_history[-4:]
    history_text = "\n".join(
        f"{'Usuario' if m['role'] == 'user' else 'Assistente'}: "
        f"{m['content'][:300] if isinstance(m['content'], str) else '[imagem]'}"
        for m in recent
    )

    try:
        response = _gemini_generate(
            model=config.REFORMULATION_MODEL,
            max_tokens=200,
            system=(
                "Voce reescreve perguntas de follow-up para serem autocontidas. "
                "Substitua pronomes e referencias vagas pelo tema correto do historico. "
                "Retorne APENAS a pergunta reescrita, sem explicacao. "
                "Se a pergunta ja for autocontida, retorne-a como esta."
            ),
            contents=(
                f"Historico recente:\n{history_text}\n\n"
                f"Pergunta atual: {question}\n\n"
                "Reescreva a pergunta para ser autocontida:"
            ),
        )
        reformulated = response.text.strip()
        if reformulated and len(reformulated) < 500:
            logger.info(
                "Query reformulada: '%s' -> '%s'",
                question[:60],
                reformulated[:60],
            )
            return reformulated
    except Exception as e:
        logger.warning("Erro na reformulacao de query: %s", e)

    return question


# -- Re-ranking com LLM (P1.1) -------------------------------------------------
def _rerank_chunks_with_llm(
    query: str,
    chunks: list[dict],
    top_n: int | None = None,
) -> list[dict]:
    """Usa Gemini Flash para reordenar chunks por relevancia real a pergunta."""
    if not config.RAG_ENABLE_RERANKING:
        return chunks
    if not chunks or len(chunks) <= 2:
        return chunks

    # Pular re-ranking se o top chunk ja tem similaridade alta — busca ja acertou
    top_sim = _safe_similarity(chunks[0].get("similarity", 0))
    if top_sim >= 0.82:
        logger.info("Re-ranking LLM pulado: top chunk similarity=%.3f >= 0.82", top_sim)
        return chunks

    if top_n is None:
        top_n = config.MAX_CONTEXT_CHUNKS

    # Montar resumos compactos para scoring (max 10 candidatos)
    candidates = chunks[:10]
    chunk_summaries = []
    for i, chunk in enumerate(candidates):
        content = (chunk.get("content") or "")[:250]
        filename = chunk.get("filename", "")
        chunk_summaries.append(f"[{i}] ({filename}) {content}")

    summaries_text = "\n---\n".join(chunk_summaries)

    try:
        response = _gemini_generate(
            model=config.REFORMULATION_MODEL,
            max_tokens=200,
            system=(
                "Voce e um ranqueador de documentos tecnicos. "
                "Dada uma pergunta e trechos de documentos, retorne os indices dos trechos "
                "mais relevantes para responder a pergunta, do mais relevante ao menos. "
                "Retorne APENAS os numeros separados por virgula. Exemplo: 3,0,7,1"
            ),
            contents=f"Pergunta: {query}\n\nTrechos:\n{summaries_text}",
        )

        ranking_text = response.text.strip()
        indices = []
        for part in ranking_text.replace(" ", "").split(","):
            try:
                idx = int(part)
                if 0 <= idx < len(candidates) and idx not in indices:
                    indices.append(idx)
            except ValueError:
                continue

        if indices:
            reranked = [candidates[i] for i in indices]
            # Adicionar chunks nao mencionados no ranking ao final
            seen = set(indices)
            for i, chunk in enumerate(candidates):
                if i not in seen:
                    reranked.append(chunk)
            # Adicionar chunks alem dos 10 candidatos ao final
            if len(chunks) > 10:
                reranked.extend(chunks[10:])
            logger.info("Re-ranking LLM aplicado: %d chunks reordenados", len(indices))
            return reranked

    except Exception as e:
        logger.warning("Erro no re-ranking LLM: %s", e)

    return chunks


# -- Resposta do Claude ---------------------------------------------------------
def ask(
    question: str,
    conversation_history: list[dict] = None,
    images: list[dict] = None,
) -> tuple[str, list[dict]]:
    """
    Responde uma pergunta usando RAG + Gemini.

    images: lista de dicts com chaves 'data' (bytes base64) e 'media_type' (ex: 'image/png').
    """
    # P0.1: Reformular query com historico para follow-ups
    search_query = _reformulate_query_with_history(question, conversation_history)

    # ── FULL CONTEXT MODE (estilo Claude Projects) ───────────────────
    if config.FULL_CONTEXT_ENABLED:
        full_context = _load_full_context_docs()
        chunks = []  # sem RAG no modo full context

        system = config.SYSTEM_PROMPT
        if full_context:
            system += (
                "\n\n<knowledge_base>\n"
                "Abaixo esta a BASE DE CONHECIMENTO COMPLETA da Maxima Sistemas. "
                "Voce tem acesso a TODOS os documentos. Use-os para responder de forma "
                "completa, detalhada e precisa. Faca conexoes entre documentos quando relevante.\n\n"
                f"{full_context}\n"
                "</knowledge_base>"
            )
        else:
            system += (
                "\n\nA base de conhecimento nao foi carregada. "
                "Responda: \"Base de conhecimento indisponivel no momento. Tente novamente.\""
            )
    else:
        # ── RAG MODE (pipeline original) ──────────────────────────────
        query_plan = _classify_query_intent(search_query)
        logger.info(
            "Roteamento da pergunta: intent=%s modules=%s doc_types=%s",
            query_plan.get("intent", "general"),
            query_plan.get("modules", []),
            query_plan.get("doc_types", []),
        )
        chunks = search_similar_chunks(search_query, query_plan=query_plan)

        # P1.1: Re-ranking com LLM
        chunks = _rerank_chunks_with_llm(search_query, chunks)

        context = build_context(chunks)
        business_rules = _load_business_rules_context()
        intent_instruction = _intent_response_instruction(query_plan)

        system = config.SYSTEM_PROMPT
        if business_rules:
            system += (
                "\n\n<business_rules>\n"
                "Abaixo esta o contexto FIXO de regras de negocio do maxPedido. "
                "Use essas regras como referencia canonica junto com os documentos recuperados.\n\n"
                f"{business_rules}\n"
                "</business_rules>"
            )

        if query_plan:
            routed_modules = query_plan.get("modules") or []
            if routed_modules:
                system += (
                    "\n\n<routing>\n"
                    f"Pergunta roteada para os modulos: {', '.join(routed_modules)}.\n"
                    "Priorize contexto e exemplos desses modulos quando houver conflito de sinais."
                    "\n</routing>"
                )

        if intent_instruction:
            system += (
                "\n\n<response_mode>\n"
                f"{intent_instruction}\n"
                "</response_mode>"
            )

        if context:
            system += (
                "\n\n<context>\n"
                "Abaixo estao os trechos relevantes dos documentos da base de conhecimento. "
                "Eles estao ORDENADOS DO MAIS RELEVANTE PARA O MENOS RELEVANTE. "
                "O atributo 'relevance' indica a similaridade com a pergunta (0-1). "
                "Priorize informacoes dos documentos com maior relevance. "
                "Use APENAS essas informacoes para responder.\n\n"
                f"{context}\n"
                "</context>"
            )
        else:
            system += (
                "\n\nNenhum documento recuperado por busca semantica foi encontrado para esta pergunta. "
                "Se o bloco business_rules acima for suficiente, responda com base nele. "
                "Caso nao haja informacao suficiente, responda exatamente:\n"
                "\"Nao encontrei essa informacao na base de conhecimento.\n\n"
                "Sugestoes:\n"
                "- Tente reformular a pergunta com termos diferentes\n"
                "- Use palavras-chave mais especificas (ex: nome do campo, tela ou erro)\n"
                "- Se precisar, abra um chamado ou consulte a equipe N2\""
            )

    # Montar conteudo da mensagem (texto + imagens) no formato Gemini
    user_parts: list[_gtypes.Part] = []
    if images:
        for img in images:
            user_parts.append(_gtypes.Part(
                inline_data=_gtypes.Blob(
                    mime_type=img["media_type"],
                    data=_base64.b64decode(img["data"]),
                )
            ))
    user_parts.append(_gtypes.Part(text=question))

    # Converter historico para formato Gemini
    gemini_contents: list[_gtypes.Content] = []
    if conversation_history:
        gemini_contents = _anthropic_msgs_to_gemini(conversation_history)
    gemini_contents.append(_gtypes.Content(role="user", parts=user_parts))

    try:
        response = _gemini_generate(
            model=config.GEMINI_MODEL,
            max_tokens=config.ASK_MAX_TOKENS,
            system=system,
            contents=gemini_contents,
        )
        if response.text:
            answer = response.text
        else:
            logger.warning("Resposta inesperada do Gemini: %s", response)
            answer = "Nao foi possivel extrair uma resposta do modelo."
    except Exception as e:
        error_str = str(e).lower()
        if "429" in str(e) or "resource_exhausted" in error_str or "rate" in error_str:
            logger.error("Rate limit do Gemini atingido: %s", e)
            answer = "O servico esta sobrecarregado no momento. Tente novamente em alguns segundos."
        elif "401" in str(e) or "403" in str(e) or "api_key" in error_str or "permission" in error_str:
            logger.error("Erro de autenticacao com Gemini: %s", e)
            answer = "Erro de configuracao do bot. Contate o administrador."
        elif "timeout" in error_str:
            logger.error("Timeout na chamada ao Gemini: %s", e)
            answer = "A consulta demorou demais. Tente reformular com uma pergunta mais curta."
        elif "connect" in error_str:
            logger.error("Erro de conexao com Gemini: %s", e)
            answer = "Nao foi possivel conectar ao servico. Tente novamente em instantes."
        else:
            logger.error("Erro ao chamar Gemini: %s", e, exc_info=True)
            answer = "Ocorreu um erro inesperado. Tente novamente."

    return answer, chunks


# -- Utilitarios ----------------------------------------------------------------
def get_stats() -> dict:
    result = supabase_rpc("get_stats", {})
    if result:
        return result[0]
    return {"total_documents": 0, "total_chunks": 0}


def list_documents() -> list[dict]:
    return supabase_select(
        "documents",
        select="filename,doc_type,chunk_count,created_at",
    )


# -- Knowledge Gaps (queries sem resposta) --------------------------------------
def log_knowledge_gap(query: str, max_similarity: float, platform: str = "discord") -> None:
    """Registra query que nao teve resposta adequada na base."""
    global _knowledge_gap_rpc_available

    if _knowledge_gap_rpc_available is False:
        try:
            _fallback_log_knowledge_gap(query, max_similarity, platform)
            logger.info(
                "Knowledge gap registrado via fallback: '%s' (sim=%.2f)",
                query[:80],
                _safe_similarity(max_similarity),
            )
        except Exception as e:
            logger.warning("Erro ao registrar knowledge gap via fallback: %s", e)
        return

    try:
        supabase_rpc(
            "upsert_knowledge_gap",
            {
                "p_query": query[:500],  # limitar tamanho
                "p_max_similarity": max_similarity,
                "p_platform": platform,
            },
        )
        _knowledge_gap_rpc_available = True
        logger.info("Knowledge gap registrado: '%s' (sim=%.2f)", query[:80], max_similarity)
    except Exception as e:
        if _is_missing_rpc_function(e, "upsert_knowledge_gap"):
            if _knowledge_gap_rpc_available is not False:
                logger.warning(
                    "RPC upsert_knowledge_gap nao encontrada no Supabase; usando fallback por tabela."
                )
            _knowledge_gap_rpc_available = False
            try:
                _fallback_log_knowledge_gap(query, max_similarity, platform)
                logger.info(
                    "Knowledge gap registrado via fallback: '%s' (sim=%.2f)",
                    query[:80],
                    _safe_similarity(max_similarity),
                )
            except Exception as fallback_error:
                logger.warning(
                    "Erro ao registrar knowledge gap via fallback: %s",
                    fallback_error,
                )
            return
        # Nao propagar erro: logging de gaps nao deve afetar a resposta ao usuario
        logger.warning("Erro ao registrar knowledge gap: %s", e)


def get_top_knowledge_gaps(limit: int = 10) -> list[dict]:
    """Retorna as queries sem resposta mais frequentes."""
    global _top_knowledge_gaps_rpc_available

    if _top_knowledge_gaps_rpc_available is False:
        try:
            return _fallback_get_top_knowledge_gaps(limit)
        except Exception as e:
            logger.error("Erro ao buscar knowledge gaps via fallback: %s", e)
            return []

    try:
        result = supabase_rpc("get_top_knowledge_gaps", {"p_limit": limit})
        _top_knowledge_gaps_rpc_available = True
        return result
    except Exception as e:
        if _is_missing_rpc_function(e, "get_top_knowledge_gaps"):
            if _top_knowledge_gaps_rpc_available is not False:
                logger.warning(
                    "RPC get_top_knowledge_gaps nao encontrada no Supabase; usando fallback por tabela."
                )
            _top_knowledge_gaps_rpc_available = False
            try:
                return _fallback_get_top_knowledge_gaps(limit)
            except Exception as fallback_error:
                logger.error(
                    "Erro ao buscar knowledge gaps via fallback: %s",
                    fallback_error,
                )
                return []
        logger.error("Erro ao buscar knowledge gaps: %s", e)
        return []

