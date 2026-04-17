"""
Gera um unico markdown de ingestao a partir dos arquivos em
documentos/gatekeeper_markdowns.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT_DIR / "documentos" / "gatekeeper_markdowns"
OUTPUT_PATH = ROOT_DIR / "documentos" / "13-GATEKEEPER-FILIPE-PADILHA.md"
SOURCE_DIR_CANDIDATES = [
    SOURCE_DIR,
    ROOT_DIR / "runtime" / "gatekeeper_export_runs",
    ROOT_DIR / "datasets",
]


TITLE_RE = re.compile(r"^#\s+.+$", re.MULTILINE)
ISSUE_NUMBER_RE = re.compile(r"GATE-(\d+)", re.IGNORECASE)
IMAGE_LINE_RE = re.compile(r"^\s*![^!]+!\s*$", re.IGNORECASE)
COLOR_TAG_RE = re.compile(r"\{color(?::#[^}]+)?\}", re.IGNORECASE)
PLACEHOLDER_COMMENT_RE = re.compile(r"nenhum coment[aá]rio eleg[ií]vel do assignee foi identificado\.?", re.IGNORECASE)
NOISE_LINE_RE = re.compile(
    r"^\s*(atualizado\s*--.*|--\d{4}-\d{2}-\d{2}.*)\s*$",
    re.IGNORECASE,
)
SQL_HEAD_RE = re.compile(
    r"^\s*(select|update|insert|delete|merge|with|from|where|join|left join|right join|inner join|group by|order by|union|and |or |on |having)\b",
    re.IGNORECASE,
)
SQL_INLINE_RE = re.compile(r"\b(select|update|insert|delete|from|where|join|group by|order by)\b", re.IGNORECASE)
QUERY_INTRO_RE = re.compile(
    r"^\s*(a query definitiva [ée] essa:?|caso voc[eê].*query.*|o c[oó]digo de usu[aá]rio .* [ée]$|a base da consulta [ée] essa:?|por causa das outras cl[aá]usulas.*|###\s+consultas utilizadas)\s*$",
    re.IGNORECASE,
)
UPPERCASE_FRAGMENT_RE = re.compile(r"^[A-Z_]+(?:\s+[A-Z_]+)*$")
SQL_FRAGMENT_RE = re.compile(
    r"^([A-Z0-9_]+\.[A-Z0-9_]+.*|[A-Z0-9_:.()'=<>-]+\s+[A-Z0-9_:.()'=<>,-]+.*)$"
)
CONSULTAS_SECTION_RE = re.compile(
    r"(?ims)^\s*(?:##+)?\s*(?:consultas utilizadas|selects? utilizados)\s*#*\s*\n.*?(?=^\s*##\s+|\Z)"
)
REUSABLE_SIGNAL_RE = re.compile(
    r"(par[âa]metr|permiss|configur|precisa|deve|necess[áa]ri|obrigat[óo]ri|"
    r"para resolver|o problema ocorre|o que acontece|motivo|causa|"
    r"comportamento|funcionalidade|regra|valida|valida[cç][ãa]o|"
    r"recomend|op[cç][ãa]o|integra[cç][ãa]o|endpoint|tabela|"
    r"vincul|sincroniz|devido|porque|fluxo|cen[áa]rio|consulta)",
    re.IGNORECASE,
)
ADMIN_NOISE_LINE_RE = re.compile(
    r"^\s*(?:.*(?:encaminhad[oa]|enviad[oa]|subir|subido|formalizar).{0,80}\b(?:n3|tech)\b.*|"
    r".*\b(?:n3|tech)\b.{0,80}(?:dev|p\.?o\.?|formaliz|corrig|verific|averigu).*$|"
    r"enviei\s+o\s+ticket\s+para\s+a?\s*tech.*|"
    r"tentei\s+(?:tamb[ée]m\s+)?(?:conex[aã]o|conectar).*(?:maxviewer|cliente).*|"
    r".*libera[cç][aã]o\s+das\s+portas.*|"
    r".*cliente\s+.*parou\s+de\s+me\s+responder.*|"
    r"foi\s+feita\s+a\s+carga.*|fiz\s+carga.*|realizei\s+.*carga.*|"
    r"fiz\s+a\s+normaliza[cç][aã]o.*|realizei\s+a\s+normaliza[cç][aã]o.*|"
    r"atualizei\s+o\s+ambiente.*|atualizei\s+o\s+banco.*|"
    r"atualizei\s+eles\s+para\s+a\s+.*vers[ãa]o.*|"
    r"ser[aá]\s+necess[áa]rio\s+pedir\s+novamente.*)\s*$",
    re.IGNORECASE,
)
LOW_VALUE_TITLE_RE = re.compile(
    r"(solicita[cç][ãa]o\s+de\s+query|limpar\s+logs|formalizar)",
    re.IGNORECASE,
)
COMMENT_HEADING_RE = re.compile(r"^###\s+(\d+)\.\s+(.*)$")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _clean(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").replace("\ufeff", "")
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def _strip_jira_markup(text: str) -> str:
    cleaned = COLOR_TAG_RE.sub("", text)
    cleaned = re.sub(r"\{\{([^}]+)\}\}", r"\1", cleaned)
    cleaned = cleaned.replace("Â", "")
    return cleaned


def _is_sql_like_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("--"):
        return True
    return bool(SQL_HEAD_RE.match(stripped))


def _prune_large_sql_blocks(text: str) -> str:
    lines = text.split("\n")
    result: list[str] = []
    sql_block: list[str] = []

    def flush_sql_block() -> None:
        nonlocal sql_block
        if not sql_block:
            return
        joined = "\n".join(sql_block).strip()
        line_count = sum(1 for line in sql_block if line.strip())
        longest_line = max((len(line) for line in sql_block), default=0)
        should_drop = len(joined) > 700 or line_count > 10 or longest_line > 280
        if not should_drop:
            result.extend(sql_block)
        sql_block = []

    for line in lines:
        stripped = line.strip()
        if _is_sql_like_line(line) or (sql_block and (not stripped or stripped.endswith(",") or stripped.endswith(";") or stripped.endswith(")"))):
            sql_block.append(line)
            continue
        flush_sql_block()
        if SQL_INLINE_RE.search(stripped) and len(stripped) > 350:
            continue
        result.append(line)

    flush_sql_block()
    return "\n".join(result)


def _clean_section_text(text: str) -> str:
    cleaned = _strip_jira_markup(text)
    cleaned = CONSULTAS_SECTION_RE.sub("", cleaned)
    cleaned = _prune_large_sql_blocks(cleaned)

    useful_lines: list[str] = []
    previous_blank = False
    skipping_query_section = False
    for raw_line in cleaned.split("\n"):
        line = raw_line.rstrip()
        stripped = line.strip()

        if skipping_query_section:
            if stripped.startswith("## ") or re.match(r"^###\s+\d+\.", stripped):
                skipping_query_section = False
            else:
                continue

        if re.match(r"^(?:##+)?\s*(?:consultas utilizadas|selects? utilizados)\s*#*\s*$", stripped, re.IGNORECASE):
            skipping_query_section = True
            continue

        if IMAGE_LINE_RE.match(stripped):
            continue
        if PLACEHOLDER_COMMENT_RE.search(stripped):
            continue
        if NOISE_LINE_RE.match(stripped):
            continue
        if ADMIN_NOISE_LINE_RE.match(stripped):
            continue
        lowered = stripped.lower()
        if "null hash" in lowered:
            continue
        if "abaixo vou colocar os detalhes" in lowered:
            continue
        if "query" in lowered and not SQL_INLINE_RE.search(stripped):
            continue
        if lowered.startswith("mas e porque") or lowered.startswith("mas e por que"):
            continue
        if lowered.startswith("por causa das outras cl"):
            continue
        if lowered.startswith("o cÃ³digo de usuÃ¡rio") or lowered.startswith("o código de usuário"):
            continue
        if lowered.startswith("a base da consulta"):
            continue
        if "nÃ£o passar" in lowered or "não passar" in lowered:
            continue

        if not stripped:
            if previous_blank:
                continue
            useful_lines.append("")
            previous_blank = True
            continue

        useful_lines.append(line)
        previous_blank = False

    cleaned = "\n".join(useful_lines)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    cleaned = re.sub(r"\n+### Consultas utilizadas\s*\n*$", "\n", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"^\s*##?SELECTS? UTILIZADOS##?\s*$", "### Consultas utilizadas", cleaned, flags=re.IGNORECASE | re.MULTILINE)
    cleaned = re.sub(r"^\s*SELECTS? UTILIZADOS:\s*$", "### Consultas utilizadas", cleaned, flags=re.IGNORECASE | re.MULTILINE)
    cleaned = re.sub(r"(### Consultas utilizadas\s*\n)(\s*\n)+", "", cleaned, flags=re.IGNORECASE)
    cleaned = _clean(cleaned)

    lines = cleaned.split("\n")
    sql_like_lines = [
        line for line in lines
        if _is_sql_like_line(line)
        or (SQL_INLINE_RE.search(line) and len(line.strip()) > 80)
        or UPPERCASE_FRAGMENT_RE.match(line.strip())
        or SQL_FRAGMENT_RE.match(line.strip())
    ]
    if len(sql_like_lines) > 10 or sum(len(line) for line in sql_like_lines) > 900:
        reduced_lines: list[str] = []
        previous_blank = False
        for raw_line in lines:
            stripped = raw_line.strip()
            if (
                _is_sql_like_line(raw_line)
                or (SQL_INLINE_RE.search(raw_line) and len(stripped) > 80)
                or UPPERCASE_FRAGMENT_RE.match(stripped)
                or SQL_FRAGMENT_RE.match(stripped)
                or QUERY_INTRO_RE.match(stripped)
            ):
                continue
            if not stripped:
                if previous_blank:
                    continue
                reduced_lines.append("")
                previous_blank = True
                continue
            reduced_lines.append(raw_line)
            previous_blank = False
        cleaned = _clean("\n".join(reduced_lines))

    return cleaned


def _comments_are_useful(text: str) -> bool:
    if not text:
        return False
    body_lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("### "):
            continue
        body_lines.append(stripped)
    joined = " ".join(body_lines).strip()
    return bool(joined)


def _body_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("### "):
            continue
        lines.append(stripped)
    return lines


def _context_is_informative(context: str) -> bool:
    for line in context.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            continue
        if stripped.lower() in {"n/a", "na", "não informado", "nao informado"}:
            continue
        return True
    return False


def _is_future_useful_ticket(title: str, context: str, comments: str) -> bool:
    body_lines = _body_lines(comments)
    if not body_lines:
        return False

    joined = " ".join(body_lines).strip()
    positive_hits = len(REUSABLE_SIGNAL_RE.findall(joined))
    admin_hits = sum(1 for line in body_lines if ADMIN_NOISE_LINE_RE.match(line))
    informative_context = _context_is_informative(context)

    if LOW_VALUE_TITLE_RE.search(title) and positive_hits == 0:
        return False
    if admin_hits and positive_hits == 0:
        return False
    if not informative_context and positive_hits == 0:
        return False
    if len(joined) < 120 and positive_hits == 0:
        return False
    if admin_hits >= 2 and positive_hits <= 1 and len(joined) < 450:
        return False

    return True


def _extract_title(text: str) -> str:
    match = TITLE_RE.search(text)
    if not match:
        raise ValueError("Titulo do issue nao encontrado.")
    return match.group(0).strip()


def _extract_between(text: str, start_heading: str, end_heading: str | None = None) -> str:
    start_token = f"## {start_heading}"
    start_idx = text.find(start_token)
    if start_idx < 0:
        return ""

    body_start = start_idx + len(start_token)
    if end_heading is None:
        body = text[body_start:]
    else:
        end_token = f"## {end_heading}"
        end_idx = text.find(end_token, body_start)
        body = text[body_start:] if end_idx < 0 else text[body_start:end_idx]
    return _clean(body)


def _extract_comments_section(text: str) -> str:
    start_token = "## Comentarios do Gatekeeper"
    start_idx = text.find(start_token)
    if start_idx < 0:
        return ""

    body_start = start_idx + len(start_token)
    remaining = text[body_start:]
    next_heading = re.search(r"(?m)^##\s+", remaining)
    if next_heading:
        remaining = remaining[:next_heading.start()]
    return _clean(remaining)


def _sort_key(path: Path) -> tuple[int, str]:
    match = ISSUE_NUMBER_RE.search(path.stem)
    return (int(match.group(1)) if match else 10**9, path.name.lower())


def _count_markdowns(path: Path) -> int:
    if not path.exists():
        return 0
    if path.is_file():
        return 1 if path.suffix.lower() == ".md" and ISSUE_NUMBER_RE.search(path.stem) else 0
    if path.name.lower() == "markdown":
        return len(list(path.glob("GATE-*.md")))
    return len(list(path.rglob("GATE-*.md")))


def _choose_source_dir() -> Path:
    best_path = SOURCE_DIR
    best_count = _count_markdowns(SOURCE_DIR)

    for candidate in SOURCE_DIR_CANDIDATES[1:]:
        if not candidate.exists():
            continue

        search_roots = [candidate]
        if candidate.name == "gatekeeper_export_runs":
            search_roots = [path for path in candidate.iterdir() if path.is_dir()]

        for root in search_roots:
            markdown_dir = root / "review" / "markdown"
            count = _count_markdowns(markdown_dir if markdown_dir.exists() else root)
            if count > best_count:
                best_path = markdown_dir if markdown_dir.exists() else root
                best_count = count

    return best_path


def _flatten_block_for_rag(text: str, *, comment_mode: bool = False) -> str:
    lines: list[str] = []
    previous_blank = False

    for raw_line in text.split("\n"):
        stripped = raw_line.strip()
        if not stripped:
            if previous_blank:
                continue
            lines.append("")
            previous_blank = True
            continue

        if stripped.startswith("## "):
            label = stripped[3:].strip().rstrip(":")
            lines.append(f"{label}:")
            previous_blank = False
            continue

        if comment_mode:
            comment_heading = COMMENT_HEADING_RE.match(stripped)
            if comment_heading:
                number = comment_heading.group(1).strip()
                header = comment_heading.group(2).strip()
                lines.append(f"Comentario {number} - {header}:")
                previous_blank = False
                continue

        if stripped.startswith("### "):
            label = stripped[4:].strip().rstrip(":")
            lines.append(f"{label}:")
            previous_blank = False
            continue

        lines.append(raw_line.rstrip())
        previous_blank = False

    return _clean("\n".join(lines))


def _build_issue_block(path: Path) -> str:
    text = _read_text(path)
    title = _extract_title(text)
    context = _clean_section_text(_extract_between(text, "Contexto do Problema", "Comentarios do Gatekeeper"))
    comments = _clean_section_text(_extract_comments_section(text))

    if not context:
        raise ValueError(f"Secao 'Contexto do Problema' ausente em {path.name}.")
    if not _comments_are_useful(comments):
        return ""
    if not _is_future_useful_ticket(title, context, comments):
        return ""

    context_rag = _flatten_block_for_rag(context)
    comments_rag = _flatten_block_for_rag(comments, comment_mode=True)

    parts = [
        title,
        "",
        "Tipo: gatekeeper_case",
        "",
        "Pergunta/Contexto:",
        "",
        context_rag,
        "",
        "Resposta do Gatekeeper:",
        "",
        comments_rag,
    ]
    return "\n".join(parts).strip()


def _clean_final_document(text: str) -> str:
    cleaned = re.sub(
        r"(?ims)^\s*###\s*Consultas utilizadas\s*\n.*?(?=^\s*##\s+|^\s*#\s+GATE-\d+\b|\Z)",
        "",
        text,
    )

    lines: list[str] = []
    skipping_query_section = False
    previous_blank = False

    for raw_line in cleaned.splitlines():
        stripped = raw_line.strip()
        lowered = stripped.lower()

        if skipping_query_section:
            if stripped.startswith("## ") or stripped.startswith("# GATE-") or re.match(r"^###\s+\d+\.", stripped):
                skipping_query_section = False
            else:
                continue

        if re.match(r"^###\s*consultas utilizadas\s*$", stripped, re.IGNORECASE):
            skipping_query_section = True
            continue
        if stripped.upper() == "NULL HASH":
            continue
        if "!image-" in lowered:
            continue

        if not stripped:
            if previous_blank:
                continue
            lines.append("")
            previous_blank = True
            continue

        lines.append(raw_line.rstrip())
        previous_blank = False

    return "\n".join(lines).strip() + "\n"


def main() -> int:
    source_dir = _choose_source_dir()
    if not source_dir.exists():
        raise SystemExit(f"Pasta nao encontrada: {SOURCE_DIR}")

    blocks = []
    skipped = 0
    for path in sorted(source_dir.glob("GATE-*.md"), key=_sort_key):
        block = _build_issue_block(path)
        if not block:
            skipped += 1
            continue
        blocks.append(block)

    final_text = _clean_final_document("\n\n".join(blocks))
    OUTPUT_PATH.write_text(final_text, encoding="utf-8")
    print(f"Fonte utilizada: {source_dir}")
    print(f"Arquivo gerado em: {OUTPUT_PATH}")
    print(f"Tickets consolidados: {len(blocks)}")
    print(f"Tickets descartados por falta de conteudo util: {skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
