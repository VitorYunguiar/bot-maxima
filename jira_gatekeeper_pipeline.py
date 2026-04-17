"""
jira_gatekeeper_pipeline.py - Pipeline dataset-first para tickets Gatekeeper.

Coleta chamados do Jira via REST API, normaliza os campos de contexto,
seleciona comentarios substantivos do gatekeeper e opcionalmente gera uma
resposta canonica validada por LLM.
"""

from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import re
import time
import zipfile
from collections import OrderedDict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import httpx
from bs4 import BeautifulSoup

import config
import rag
from bot_common import normalize_text

logger = logging.getLogger(__name__)

DEFAULT_JQL = "project = Gatekeeper AND assignee = filipe.padilha"
DEFAULT_OUTPUT_DIR = Path("datasets") / "gatekeeper_filipe"
CHECKPOINT_OVERLAP_MINUTES = 10
PROMPT_VERSION = "gatekeeper-filipe-v1"
RETRY_STATUS_CODES = {408, 409, 425, 429, 500, 502, 503, 504}

_FIELD_SPECS = OrderedDict(
    [
        (
            "passos_reproduzir",
            {
                "label": "Passos para reproduzir",
                "aliases": ["Passos para reproduzir"],
                "fallback_id": "customfield_10221",
            },
        ),
        (
            "resultado_apresentado",
            {
                "label": "Resultado apresentado",
                "aliases": ["Resultado apresentado"],
                "fallback_id": "customfield_10222",
            },
        ),
        (
            "resultado_esperado",
            {
                "label": "Resultado esperado",
                "aliases": ["Resultado esperado"],
                "fallback_id": "customfield_10223",
            },
        ),
        (
            "descricao",
            {
                "label": "Descrição",
                "aliases": ["Descrição", "Descricao", "Description"],
                "fallback_id": "description",
            },
        ),
        (
            "assunto",
            {
                "label": "Assunto",
                "aliases": ["Assunto"],
                "fallback_id": "customfield_10320",
            },
        ),
        (
            "erp_cliente",
            {
                "label": "Qual ERP do cliente?",
                "aliases": ["Qual ERP do cliente?", "ERP do cliente", "Qual ERP do cliente"],
                "fallback_id": "customfield_10232",
            },
        ),
        (
            "natureza",
            {
                "label": "Natureza",
                "aliases": ["Natureza"],
                "fallback_id": "customfield_10407",
            },
        ),
    ]
)

_COMMENT_TECHNICAL_HINTS = (
    "parametro",
    "configur",
    "valid",
    "verific",
    "evidenc",
    "orient",
    "necessar",
    "deve",
    "ajust",
    "corrig",
    "fluxo",
    "comport",
    "regra",
    "api",
    "erp",
    "banco",
    "query",
    "tabela",
    "campo",
    "coluna",
    "sql",
    "select",
    "from",
    "join",
    "where",
    "update",
    "insert",
    "delete",
    "resultado",
    "esperado",
    "apresentado",
    "causa",
    "analise",
    "analis",
    "diagnost",
    "critica",
    "retorno",
    "reprocess",
    "permiss",
    "rotina",
)
_ATTACHMENT_TERMS_RE = re.compile(
    r"\b(anexo|anexos|planilha|planilhas|print|prints|imagem|imagens|screenshot|arquivo|arquivos)\b",
    flags=re.IGNORECASE,
)
_SQL_RE = re.compile(r"\b(select|update|insert|delete|from|join|where|union|group\s+by|order\s+by)\b", re.IGNORECASE)
_GREETING_RE = re.compile(r"^(bom dia|boa tarde|boa noite|ola|ol[aá])[\s,!.:;-]*$", re.IGNORECASE)
_SIGNOFF_RE = re.compile(r"^(att|atts|atenciosamente|obrigado|obrigada|abracos|abra[cç]os|valeu)[\s,!.:;-]*$", re.IGNORECASE)
_NON_SUBSTANTIVE_RE = re.compile(
    r"^(ok|feito|ajustado|validado|verificado|encaminhado|alinhado|resolvido|segue anexo|conforme anexo)[\s.!-]*$",
    re.IGNORECASE,
)
_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.IGNORECASE | re.DOTALL)
_ORDER_BY_RE = re.compile(r"\border\s+by\b.*$", re.IGNORECASE | re.DOTALL)


@dataclass
class JiraCredentials:
    base_url: str
    username: str | None = None
    password: str | None = None
    api_token: str | None = None
    session_cookie: str | None = None
    timeout_seconds: float = 60.0
    max_retries: int = 3
    retry_base_seconds: float = 1.0


def _normalize_field_name(value: str) -> str:
    return normalize_text(value or "")


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _utc_now_iso() -> str:
    return _utc_now().isoformat()


def _safe_strip(value: Any) -> str:
    return str(value or "").strip()


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(maximum, value))


def _parse_json_payload(text: str) -> dict[str, Any]:
    raw = _safe_strip(text)
    if not raw:
        raise ValueError("Resposta JSON vazia.")

    fenced = _JSON_BLOCK_RE.search(raw)
    if fenced:
        raw = fenced.group(1).strip()

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start < 0 or end <= start:
            raise
        parsed = json.loads(raw[start : end + 1])

    if not isinstance(parsed, dict):
        raise ValueError("Resposta JSON invalida: esperado objeto.")
    return parsed


def _format_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def _write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(_format_json(data), encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def _remove_path_with_retry(path: Path, retries: int = 3, delay_seconds: float = 0.3) -> bool:
    if not path.exists():
        return True
    for attempt in range(retries + 1):
        try:
            if path.is_dir():
                for child in path.iterdir():
                    _remove_path_with_retry(child, retries=retries, delay_seconds=delay_seconds)
                if path.exists():
                    path.rmdir()
            else:
                path.unlink()
            return True
        except PermissionError:
            try:
                os.chmod(path, 0o666)
            except OSError:
                pass
            if attempt >= retries:
                logger.warning("Nao foi possivel remover %s durante o refresh; seguindo sem excluir.", path)
                return False
            time.sleep(delay_seconds * (attempt + 1))
        except OSError:
            if attempt >= retries:
                logger.warning("Nao foi possivel remover %s durante o refresh; seguindo sem excluir.", path)
                return False
            time.sleep(delay_seconds * (attempt + 1))
    return not path.exists()


def _parse_datetime(value: str | None) -> datetime | None:
    raw = _safe_strip(value)
    if not raw:
        return None

    normalized = raw.replace("Z", "+00:00")
    if re.match(r".*[+-]\d{4}$", normalized):
        normalized = f"{normalized[:-5]}{normalized[-5:-2]}:{normalized[-2:]}"

    formats = (
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S%z",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d",
    )
    for fmt in formats:
        try:
            parsed = datetime.strptime(normalized, fmt)
            if parsed.tzinfo is None:
                return parsed.replace(tzinfo=timezone.utc)
            return parsed
        except ValueError:
            continue

    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError(f"Data invalida: {raw!r}") from exc
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed


def _format_jql_datetime(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M")


def _strip_order_by(jql: str) -> str:
    base = _ORDER_BY_RE.sub("", jql or "").strip()
    return base or DEFAULT_JQL


def build_incremental_jql(base_jql: str, since_updated: datetime | None) -> str:
    clean_base = _strip_order_by(base_jql)
    if since_updated is None:
        return f"{clean_base} ORDER BY updated ASC, key ASC"
    return (
        f"({clean_base}) AND updated >= \"{_format_jql_datetime(since_updated)}\" "
        "ORDER BY updated ASC, key ASC"
    )


def discover_field_ids(fields_payload: list[dict[str, Any]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for item in fields_payload or []:
        field_name = _normalize_field_name(item.get("name", ""))
        field_id = _safe_strip(item.get("id"))
        if field_name and field_id and field_name not in lookup:
            lookup[field_name] = field_id

    resolved: dict[str, str] = {}
    for slug, spec in _FIELD_SPECS.items():
        field_id = ""
        for alias in spec["aliases"]:
            normalized = _normalize_field_name(alias)
            if normalized in lookup:
                field_id = lookup[normalized]
                break
        resolved[slug] = field_id or spec["fallback_id"]
    return resolved


def _node_text(node: Any) -> str:
    if node is None:
        return ""
    if isinstance(node, str):
        return node
    if isinstance(node, list):
        return "".join(_node_text(item) for item in node)
    if not isinstance(node, dict):
        return str(node)

    node_type = node.get("type", "")
    content = node.get("content") or []

    if node_type == "text":
        return node.get("text") or ""
    if node_type == "hardBreak":
        return "\n"
    if node_type == "mention":
        attrs = node.get("attrs") or {}
        return attrs.get("text") or attrs.get("id") or ""
    if node_type == "emoji":
        attrs = node.get("attrs") or {}
        return attrs.get("text") or attrs.get("shortName") or ""
    if node_type == "codeBlock":
        inner = "".join(_node_text(item) for item in content).strip("\n")
        return f"```\n{inner}\n```\n\n" if inner else ""
    if node_type in {"paragraph", "heading", "blockquote"}:
        inner = "".join(_node_text(item) for item in content).strip()
        return f"{inner}\n\n" if inner else ""
    if node_type == "bulletList":
        lines: list[str] = []
        for item in content:
            item_text = _node_text(item).strip()
            if not item_text:
                continue
            item_lines = item_text.splitlines()
            lines.append(f"- {item_lines[0]}")
            for extra in item_lines[1:]:
                lines.append(f"  {extra}")
        return "\n".join(lines) + ("\n\n" if lines else "")
    if node_type == "orderedList":
        lines = []
        for index, item in enumerate(content, start=1):
            item_text = _node_text(item).strip()
            if not item_text:
                continue
            item_lines = item_text.splitlines()
            lines.append(f"{index}. {item_lines[0]}")
            for extra in item_lines[1:]:
                lines.append(f"   {extra}")
        return "\n".join(lines) + ("\n\n" if lines else "")
    if node_type == "listItem":
        parts = [_node_text(item).strip() for item in content]
        return "\n".join(part for part in parts if part).strip()

    return "".join(_node_text(item) for item in content)


def _html_to_text(value: str) -> str:
    soup = BeautifulSoup(value or "", "html.parser")
    for tag in soup.find_all("br"):
        tag.replace_with("\n")
    for tag in soup.find_all("li"):
        text = tag.get_text(" ", strip=True)
        tag.replace_with(f"- {text}\n")
    for tag in soup.find_all("pre"):
        text = tag.get_text("\n", strip=False).strip("\n")
        tag.replace_with(f"```\n{text}\n```\n")
    for tag in soup.find_all(("p", "div", "section", "tr")):
        text = tag.get_text(" ", strip=True)
        if text:
            tag.replace_with(f"{text}\n\n")
    extracted = soup.get_text("\n", strip=False)
    return _clean_text_block(extracted)


def _clean_text_block(value: str) -> str:
    lines = [line.rstrip() for line in str(value or "").replace("\r", "").split("\n")]
    cleaned: list[str] = []
    previous_blank = False
    for line in lines:
        if not line.strip():
            if previous_blank:
                continue
            cleaned.append("")
            previous_blank = True
            continue
        cleaned.append(line.strip())
        previous_blank = False
    return "\n".join(cleaned).strip()


def jira_value_to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        if "<" in value and ">" in value:
            return _html_to_text(value)
        return _clean_text_block(value)
    if isinstance(value, dict):
        for scalar_key in ("value", "name", "displayName"):
            scalar_value = value.get(scalar_key)
            if isinstance(scalar_value, str) and scalar_value.strip():
                return _clean_text_block(scalar_value)
        if value.get("type") == "doc" or "content" in value:
            return _clean_text_block(_node_text(value))
        if "body" in value:
            return jira_value_to_text(value["body"])
        return _clean_text_block(json.dumps(value, ensure_ascii=False))
    if isinstance(value, list):
        parts = [jira_value_to_text(item) for item in value]
        return _clean_text_block("\n".join(part for part in parts if part))
    return _clean_text_block(str(value))


def clean_comment_text(text: str) -> str:
    lines = [line.rstrip() for line in str(text or "").replace("\r", "").split("\n")]

    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    if lines and _GREETING_RE.match(lines[0].strip()) and len(lines[0].strip()) <= 20:
        lines.pop(0)

    while lines and _SIGNOFF_RE.match(lines[-1].strip()) and len(lines[-1].strip()) <= 25:
        lines.pop()

    return _clean_text_block("\n".join(lines))


def substantive_comment_score(text: str) -> int:
    clean = clean_comment_text(text)
    normalized = normalize_text(clean)
    if not normalized:
        return 0
    if _NON_SUBSTANTIVE_RE.match(clean):
        return 0

    score = 0
    if len(clean) >= 80:
        score += 1
    if len(clean) >= 220:
        score += 1
    if _SQL_RE.search(clean):
        score += 3

    technical_hits = sum(1 for token in _COMMENT_TECHNICAL_HINTS if token in normalized)
    if technical_hits >= 1:
        score += 1
    if technical_hits >= 4:
        score += 1

    line_count = sum(1 for line in clean.splitlines() if line.strip())
    if line_count >= 3:
        score += 1

    if re.search(r"\b(necess[aá]rio|deve|recomenda|orienta|causa|motivo|correto|incorreto|diverg[êe]ncia)\b", clean, re.IGNORECASE):
        score += 1

    return score


def is_substantive_comment(text: str) -> bool:
    return substantive_comment_score(text) >= 2


def parse_assignee_aliases(raw: str | None) -> list[str]:
    text = _safe_strip(raw)
    if not text:
        return []

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        parsed = None

    aliases: list[str] = []
    if isinstance(parsed, dict):
        for values in parsed.values():
            if isinstance(values, list):
                aliases.extend(str(item) for item in values if str(item).strip())
            elif isinstance(values, str) and values.strip():
                aliases.append(values)
    elif isinstance(parsed, list):
        aliases.extend(str(item) for item in parsed if str(item).strip())
    elif isinstance(parsed, str):
        aliases.extend(part.strip() for part in re.split(r"[|,;]", parsed) if part.strip())
    else:
        aliases.extend(part.strip() for part in re.split(r"[|,;]", text) if part.strip())
    return aliases


def build_author_aliases(issue: dict[str, Any], global_aliases: list[str] | None = None) -> set[str]:
    fields = issue.get("fields") or {}
    assignee = fields.get("assignee") or {}
    raw_candidates = [
        assignee.get("displayName"),
        assignee.get("name"),
        assignee.get("key"),
        assignee.get("emailAddress"),
        *(global_aliases or []),
    ]

    aliases: set[str] = set()
    for candidate in raw_candidates:
        raw = _safe_strip(candidate)
        if not raw:
            continue
        aliases.add(_normalize_field_name(raw))
        if "@" in raw:
            aliases.add(_normalize_field_name(raw.split("@", 1)[0]))
    return {alias for alias in aliases if alias}


def comment_author_matches_assignee(comment: dict[str, Any], author_aliases: set[str]) -> bool:
    author = comment.get("author") or {}
    raw_candidates = [
        author.get("displayName"),
        author.get("name"),
        author.get("key"),
        author.get("emailAddress"),
    ]
    for candidate in raw_candidates:
        raw = _safe_strip(candidate)
        if not raw:
            continue
        normalized = _normalize_field_name(raw)
        if normalized in author_aliases:
            return True
        if "@" in raw and _normalize_field_name(raw.split("@", 1)[0]) in author_aliases:
            return True
    return False


def _normalize_attachment(item: dict[str, Any]) -> dict[str, Any]:
    author = item.get("author") or {}
    return {
        "id": _safe_strip(item.get("id")),
        "filename": _safe_strip(item.get("filename")),
        "mime_type": _safe_strip(item.get("mimeType")),
        "size": int(item.get("size") or 0),
        "created": _safe_strip(item.get("created")),
        "author": _safe_strip(author.get("displayName") or author.get("name") or author.get("emailAddress")),
        "content_url": _safe_strip(item.get("content")),
    }


def _context_sections_from_issue(issue: dict[str, Any], field_ids: dict[str, str]) -> OrderedDict[str, str]:
    fields = issue.get("fields") or {}
    sections = OrderedDict()
    for slug in ("passos_reproduzir", "resultado_apresentado", "resultado_esperado", "descricao"):
        spec = _FIELD_SPECS[slug]
        field_id = field_ids.get(slug) or spec["fallback_id"]
        sections[spec["label"]] = jira_value_to_text(fields.get(field_id))
    return sections


def build_problem_context(context_sections: OrderedDict[str, str]) -> str:
    parts: list[str] = []
    for label, value in context_sections.items():
        if not _safe_strip(value):
            continue
        parts.append(f"## {label}\n{value.strip()}")
    return "\n\n".join(parts).strip()


def _normalize_comments(issue: dict[str, Any], author_aliases: set[str]) -> list[dict[str, Any]]:
    fields = issue.get("fields") or {}
    comment_block = fields.get("comment") or {}
    comments = comment_block.get("comments") or []
    normalized: list[dict[str, Any]] = []
    for item in comments:
        raw_body = jira_value_to_text(item.get("body"))
        clean_body = clean_comment_text(raw_body)
        normalized.append(
            {
                "id": _safe_strip(item.get("id")),
                "author": _safe_strip(
                    (item.get("author") or {}).get("displayName")
                    or (item.get("author") or {}).get("name")
                    or (item.get("author") or {}).get("emailAddress")
                ),
                "created": _safe_strip(item.get("created")),
                "updated": _safe_strip(item.get("updated")),
                "raw_body": raw_body,
                "clean_body": clean_body,
                "author_matches_assignee": comment_author_matches_assignee(item, author_aliases),
                "substantive_score": substantive_comment_score(clean_body),
                "is_substantive": is_substantive_comment(clean_body),
            }
        )
    return normalized


def select_gatekeeper_comments(comments: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    eligible = [comment for comment in comments if comment.get("author_matches_assignee")]
    substantive = [comment for comment in eligible if comment.get("is_substantive")]
    return eligible, [comment["id"] for comment in substantive if comment.get("id")]


def _attachment_dependency(problem_context: str, comments: list[dict[str, Any]], attachments: list[dict[str, Any]]) -> bool:
    if not attachments:
        return False
    all_comment_text = "\n\n".join(comment.get("clean_body", "") for comment in comments if comment.get("clean_body"))
    selected_text = "\n\n".join(comment.get("clean_body", "") for comment in comments if comment.get("is_substantive"))
    combined = "\n".join([problem_context, all_comment_text]).strip()
    if not _ATTACHMENT_TERMS_RE.search(combined):
        return False

    if not selected_text:
        return True

    if _SQL_RE.search(selected_text):
        return False

    technical_hits = sum(1 for token in _COMMENT_TECHNICAL_HINTS if token in normalize_text(selected_text))
    return len(selected_text) < 180 or technical_hits < 2


def calculate_confidence(
    *,
    context_sections: OrderedDict[str, str],
    substantive_comment_ids: list[str],
    grounded_approved: bool,
    requires_attachment_review: bool,
    llm_used: bool,
) -> float:
    completeness_ratio = sum(1 for value in context_sections.values() if _safe_strip(value)) / len(context_sections)
    score = 0.2
    score += completeness_ratio * 0.3
    if substantive_comment_ids:
        score += 0.25
    if llm_used and grounded_approved:
        score += 0.25
    if requires_attachment_review:
        score -= 0.2
    return round(_clamp(score), 4)


def build_review_reason(
    quality_flags: list[str],
    missing_sections: list[str],
    grounded_approved: bool,
    *,
    has_primary_comments: bool,
    confidence_below_threshold: bool,
) -> str:
    reasons: list[str] = []
    if missing_sections:
        reasons.append(f"faltam campos de contexto: {', '.join(missing_sections)}")
    if "needs_review" in quality_flags and not has_primary_comments:
        reasons.append("sem comentario substantivo do assignee")
    elif confidence_below_threshold:
        reasons.append("confianca abaixo do limiar de revisao")
    if "requires_attachment_review" in quality_flags:
        reasons.append("comentario depende de anexo/planilha/print")
    if "grounding_failed" in quality_flags and not grounded_approved:
        reasons.append("verificador de groundedness reprovou a resposta")
    return "; ".join(reasons) or "pronto para validacao manual"


class JiraApiClient:
    def __init__(self, credentials: JiraCredentials):
        self.credentials = credentials
        headers = {"Accept": "application/json"}
        if credentials.session_cookie:
            headers["Cookie"] = credentials.session_cookie
        auth = None
        secret = credentials.api_token or credentials.password
        if credentials.username and secret:
            auth = (credentials.username, secret)
        self._client = httpx.Client(
            base_url=credentials.base_url.rstrip("/"),
            headers=headers,
            auth=auth,
            timeout=credentials.timeout_seconds,
            trust_env=False,
        )

    def close(self) -> None:
        self._client.close()

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ):
        last_error: Exception | None = None
        for attempt in range(self.credentials.max_retries + 1):
            try:
                response = self._client.request(method, path, params=params, json=json_body)
                if response.status_code in RETRY_STATUS_CODES and attempt < self.credentials.max_retries:
                    delay = self.credentials.retry_base_seconds * (2 ** attempt)
                    logger.warning(
                        "Jira retornou %s para %s %s. Tentativa %s/%s, aguardando %.1fs.",
                        response.status_code,
                        method,
                        path,
                        attempt + 1,
                        self.credentials.max_retries,
                        delay,
                    )
                    time.sleep(delay)
                    continue
                response.raise_for_status()
                if response.headers.get("content-type", "").lower().startswith("application/json"):
                    return response.json()
                return response.text
            except (httpx.HTTPError, httpx.NetworkError) as exc:
                last_error = exc
                if attempt >= self.credentials.max_retries:
                    break
                delay = self.credentials.retry_base_seconds * (2 ** attempt)
                logger.warning(
                    "Erro ao consultar Jira (%s %s): %s. Tentativa %s/%s, aguardando %.1fs.",
                    method,
                    path,
                    exc,
                    attempt + 1,
                    self.credentials.max_retries,
                    delay,
                )
                time.sleep(delay)
        assert last_error is not None
        raise last_error

    def fetch_fields(self) -> list[dict[str, Any]]:
        return self._request("GET", "/rest/api/2/field")

    def search_issues(self, jql: str, *, limit: int | None = None, page_size: int = 100) -> list[dict[str, Any]]:
        issues: list[dict[str, Any]] = []
        start_at = 0
        total = float("inf")

        while start_at < total and (limit is None or len(issues) < limit):
            max_results = page_size if limit is None else min(page_size, limit - len(issues))
            payload = {
                "jql": jql,
                "startAt": start_at,
                "maxResults": max_results,
                "fields": ["summary", "updated"],
            }
            data = self._request("POST", "/rest/api/2/search", json_body=payload)
            total = int(data.get("total") or 0)
            page_items = data.get("issues") or []
            if not page_items:
                break
            issues.extend(page_items)
            start_at += len(page_items)
        return issues

    def fetch_issue_detail(self, issue_key: str, field_ids: dict[str, str]) -> dict[str, Any]:
        base_fields = {
            "summary",
            "description",
            "assignee",
            "reporter",
            "status",
            "created",
            "updated",
            "attachment",
            "comment",
        }
        for slug in ("passos_reproduzir", "resultado_apresentado", "resultado_esperado", "assunto", "erp_cliente", "natureza"):
            field_id = field_ids.get(slug)
            if field_id:
                base_fields.add(field_id)

        issue = self._request(
            "GET",
            f"/rest/api/2/issue/{quote(issue_key)}",
            params={"fields": ",".join(sorted(base_fields))},
        )

        comment_block = ((issue.get("fields") or {}).get("comment") or {})
        existing_comments = comment_block.get("comments") or []
        total = int(comment_block.get("total") or len(existing_comments))
        if total > len(existing_comments):
            issue.setdefault("fields", {})["comment"] = self.fetch_issue_comments(issue_key)
        return issue

    def fetch_issue_comments(self, issue_key: str, *, page_size: int = 100) -> dict[str, Any]:
        comments: list[dict[str, Any]] = []
        start_at = 0
        total = float("inf")
        while start_at < total:
            data = self._request(
                "GET",
                f"/rest/api/2/issue/{quote(issue_key)}/comment",
                params={"startAt": start_at, "maxResults": page_size},
            )
            total = int(data.get("total") or 0)
            page_items = data.get("comments") or []
            if not page_items:
                break
            comments.extend(page_items)
            start_at += len(page_items)
        return {
            "comments": comments,
            "total": len(comments),
            "startAt": 0,
            "maxResults": len(comments),
        }

    def search_users(self, search_term: str) -> list[dict[str, Any]]:
        term = _safe_strip(search_term)
        if not term:
            return []

        endpoint = _safe_strip(getattr(config, "JIRA_USER_SEARCH_PATH", "")) or "/rest/api/2/user/search"
        results: list[dict[str, Any]] = []
        seen: set[str] = set()

        candidate_params = [
            {"username": term},
            {"query": term},
        ]
        for params in candidate_params:
            try:
                data = self._request("GET", endpoint, params=params)
            except Exception:
                continue
            if not isinstance(data, list):
                continue
            for item in data:
                key = _safe_strip(item.get("key") or item.get("name") or item.get("emailAddress") or item.get("displayName"))
                if key and key not in seen:
                    seen.add(key)
                    results.append(item)
            if results:
                break
        return results


class GatekeeperLlmProcessor:
    def __init__(self, model: str | None = None):
        provider = (config.LLM_PROVIDER or "gemini").strip().lower()
        if model:
            self.model = model
        elif provider == "openai":
            self.model = config.OPENAI_MODEL
        else:
            self.model = config.GEMINI_MODEL
        self.provider = provider

    def _generate_text(self, *, system: str, user: str, max_tokens: int = 2048) -> str:
        response = rag._gemini_generate(
            self.model,
            system=system,
            contents=user,
            max_tokens=max_tokens,
        )
        return _safe_strip(getattr(response, "text", ""))

    def extract_facts(self, *, problem_context: str, comment_text: str) -> dict[str, Any]:
        system = (
            "Voce extrai fatos estruturados de comentarios tecnicos do Gatekeeper.\n"
            "Retorne JSON puro, sem markdown, sem texto extra.\n"
            "Nao invente fatos e nao use conhecimento externo.\n"
            "Se algo nao estiver escrito, retorne string vazia ou lista vazia."
        )
        user = (
            "Extraia os fatos do comentario abaixo.\n"
            "Use obrigatoriamente as chaves: causa, evidencias, acao_recomendada, parametros, sql, "
            "responsavel, limitacoes, proximo_passo.\n"
            "As chaves evidencias, acao_recomendada, parametros, sql e limitacoes devem ser listas.\n\n"
            f"<contexto_problema>\n{problem_context}\n</contexto_problema>\n\n"
            f"<comentario_gatekeeper>\n{comment_text}\n</comentario_gatekeeper>"
        )
        parsed = _parse_json_payload(self._generate_text(system=system, user=user, max_tokens=1800))
        return {
            "causa": _safe_strip(parsed.get("causa")),
            "evidencias": [str(item).strip() for item in parsed.get("evidencias", []) if str(item).strip()],
            "acao_recomendada": [str(item).strip() for item in parsed.get("acao_recomendada", []) if str(item).strip()],
            "parametros": [str(item).strip() for item in parsed.get("parametros", []) if str(item).strip()],
            "sql": [str(item).strip() for item in parsed.get("sql", []) if str(item).strip()],
            "responsavel": _safe_strip(parsed.get("responsavel")),
            "limitacoes": [str(item).strip() for item in parsed.get("limitacoes", []) if str(item).strip()],
            "proximo_passo": _safe_strip(parsed.get("proximo_passo")),
        }

    def canonicalize_answer(self, *, problem_context: str, facts: dict[str, Any]) -> str:
        system = (
            "Voce reescreve uma resposta tecnica do Gatekeeper para uma base de conhecimento.\n"
            "Use apenas os fatos recebidos. Nao invente, nao extrapole e nao cite que usou JSON.\n"
            "Escreva em portugues brasileiro, tom tecnico, direto e auditavel."
        )
        user = (
            "Gere uma resposta canonica curta, mas completa, baseada exclusivamente nos fatos.\n"
            "Se houver SQL relevante, mantenha em bloco de codigo.\n"
            "Nao mencione anexos como evidencia principal sem explicar a analise textual.\n\n"
            f"<contexto_problema>\n{problem_context}\n</contexto_problema>\n\n"
            f"<fatos>\n{json.dumps(facts, ensure_ascii=False, indent=2)}\n</fatos>"
        )
        return self._generate_text(system=system, user=user, max_tokens=1800)

    def verify_groundedness(self, *, answer: str, supporting_text: str) -> dict[str, Any]:
        system = (
            "Voce valida se uma resposta esta totalmente suportada pelo texto-fonte.\n"
            "Retorne JSON puro com as chaves: approved, unsupported_claims, notes.\n"
            "approved deve ser true somente se todas as afirmacoes factuais estiverem no texto-fonte."
        )
        user = (
            f"<texto_fonte>\n{supporting_text}\n</texto_fonte>\n\n"
            f"<resposta>\n{answer}\n</resposta>"
        )
        parsed = _parse_json_payload(self._generate_text(system=system, user=user, max_tokens=1200))
        unsupported = [str(item).strip() for item in parsed.get("unsupported_claims", []) if str(item).strip()]
        approved = bool(parsed.get("approved")) and not unsupported
        return {
            "approved": approved,
            "unsupported_claims": unsupported,
            "notes": _safe_strip(parsed.get("notes")),
        }


class GatekeeperDatasetPipeline:
    def __init__(
        self,
        *,
        jira_client: JiraApiClient,
        output_dir: Path,
        review_threshold: float = 0.75,
        llm_processor: GatekeeperLlmProcessor | None = None,
        no_llm: bool = False,
        assignee_aliases: list[str] | None = None,
    ):
        self.jira_client = jira_client
        self.output_dir = Path(output_dir)
        self.review_threshold = review_threshold
        self.llm_processor = None if no_llm else llm_processor
        self.no_llm = no_llm
        self.assignee_aliases = assignee_aliases or []
        self._user_alias_cache: dict[str, set[str]] = {}

    def _checkpoint_path(self) -> Path:
        return self.output_dir / "checkpoint.json"

    def _load_checkpoint(self) -> dict[str, Any]:
        path = self._checkpoint_path()
        if not path.exists():
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            logger.warning("Checkpoint invalido em %s; ignorando.", path)
            return {}

    def _save_checkpoint(self, checkpoint: dict[str, Any]) -> None:
        _write_json(self._checkpoint_path(), checkpoint)

    def _prepare_output_dir(self, *, full_refresh: bool) -> None:
        self.output_dir.mkdir(parents=True, exist_ok=True)
        for relative in ("raw/issues", "normalized", "gold", "review/markdown"):
            (self.output_dir / relative).mkdir(parents=True, exist_ok=True)

        if not full_refresh:
            return

        for relative in ("raw/issues", "review/markdown"):
            target = self.output_dir / relative
            if target.exists():
                _remove_path_with_retry(target)
                target.mkdir(parents=True, exist_ok=True)

        for relative in (
            "raw/fields.json",
            "raw/manifest.json",
            "normalized/issues.jsonl",
            "gold/pairs.jsonl",
            "review/review.csv",
            "review/review_bundle.zip",
        ):
            target = self.output_dir / relative
            if target.exists():
                _remove_path_with_retry(target)

    def _resolve_since_updated(self, *, since_updated: str | None, full_refresh: bool) -> datetime | None:
        if full_refresh:
            return None
        if since_updated:
            return _parse_datetime(since_updated)

        checkpoint = self._load_checkpoint()
        last_updated = _parse_datetime(checkpoint.get("last_updated"))
        if not last_updated:
            return None
        return last_updated - timedelta(minutes=CHECKPOINT_OVERLAP_MINUTES)

    def _fetch_assignee_aliases_from_jira(self, issue: dict[str, Any]) -> set[str]:
        fields = issue.get("fields") or {}
        assignee = fields.get("assignee") or {}
        search_candidates = [
            _safe_strip(assignee.get("name")),
            _safe_strip(assignee.get("key")),
            _safe_strip(assignee.get("emailAddress")).split("@", 1)[0] if _safe_strip(assignee.get("emailAddress")) else "",
            _safe_strip(assignee.get("displayName")),
        ]

        aliases: set[str] = set()
        for candidate in search_candidates:
            term = _safe_strip(candidate)
            if not term:
                continue
            cache_key = _normalize_field_name(term)
            if cache_key in self._user_alias_cache:
                aliases.update(self._user_alias_cache[cache_key])
                continue

            resolved: set[str] = set()
            if hasattr(self.jira_client, "search_users"):
                for user in self.jira_client.search_users(term) or []:
                    for raw in (
                        user.get("displayName"),
                        user.get("name"),
                        user.get("key"),
                        user.get("emailAddress"),
                    ):
                        value = _safe_strip(raw)
                        if not value:
                            continue
                        resolved.add(_normalize_field_name(value))
                        if "@" in value:
                            resolved.add(_normalize_field_name(value.split("@", 1)[0]))
            self._user_alias_cache[cache_key] = resolved
            aliases.update(resolved)
        return aliases

    def _normalize_issue(self, issue: dict[str, Any], field_ids: dict[str, str]) -> dict[str, Any]:
        fields = issue.get("fields") or {}
        author_aliases = build_author_aliases(issue, self.assignee_aliases)
        author_aliases.update(self._fetch_assignee_aliases_from_jira(issue))
        context_sections = _context_sections_from_issue(issue, field_ids)
        problem_context = build_problem_context(context_sections)
        attachments = [_normalize_attachment(item) for item in fields.get("attachment") or []]
        comments = _normalize_comments(issue, author_aliases)
        gatekeeper_comments, primary_comment_ids = select_gatekeeper_comments(comments)
        missing_sections = [label for label, text in context_sections.items() if not _safe_strip(text)]
        requires_attachment_review = _attachment_dependency(problem_context, gatekeeper_comments, attachments)

        quality_flags: list[str] = []
        if missing_sections:
            quality_flags.append("missing_context_sections")
        if not primary_comment_ids:
            quality_flags.append("needs_review")
        if requires_attachment_review:
            quality_flags.append("requires_attachment_review")

        return {
            "issue_key": issue.get("key"),
            "summary": _safe_strip(fields.get("summary")),
            "status": _safe_strip((fields.get("status") or {}).get("name")),
            "created": _safe_strip(fields.get("created")),
            "updated": _safe_strip(fields.get("updated")),
            "reporter": _safe_strip(
                (fields.get("reporter") or {}).get("displayName")
                or (fields.get("reporter") or {}).get("name")
                or (fields.get("reporter") or {}).get("emailAddress")
            ),
            "assignee": _safe_strip(
                (fields.get("assignee") or {}).get("displayName")
                or (fields.get("assignee") or {}).get("name")
                or (fields.get("assignee") or {}).get("emailAddress")
            ),
            "metadata": {
                "assunto": jira_value_to_text(fields.get(field_ids.get("assunto", ""))),
                "erp_cliente": jira_value_to_text(fields.get(field_ids.get("erp_cliente", ""))),
                "natureza": jira_value_to_text(fields.get(field_ids.get("natureza", ""))),
            },
            "context_sections": context_sections,
            "problem_context": problem_context,
            "all_comments": comments,
            "gatekeeper_comments": gatekeeper_comments,
            "primary_comment_ids": primary_comment_ids,
            "attachment_refs": attachments,
            "missing_context_sections": missing_sections,
            "quality_flags": quality_flags,
            "requires_attachment_review": requires_attachment_review,
        }

    def _generate_gold(self, normalized_issue: dict[str, Any]) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
        if self.no_llm or self.llm_processor is None:
            return None, None
        if not normalized_issue["primary_comment_ids"]:
            return None, None

        selected_comments = [
            comment
            for comment in normalized_issue["gatekeeper_comments"]
            if comment.get("id") in set(normalized_issue["primary_comment_ids"])
        ]
        supporting_text = "\n\n".join(comment.get("clean_body", "") for comment in selected_comments if comment.get("clean_body"))
        if not supporting_text:
            return None, None

        try:
            facts = self.llm_processor.extract_facts(
                problem_context=normalized_issue["problem_context"],
                comment_text=supporting_text,
            )
            answer = self.llm_processor.canonicalize_answer(
                problem_context=normalized_issue["problem_context"],
                facts=facts,
            )
            verification = self.llm_processor.verify_groundedness(
                answer=answer,
                supporting_text=supporting_text,
            )
        except Exception as exc:
            logger.exception("Falha ao gerar gold para %s: %s", normalized_issue["issue_key"], exc)
            normalized_issue["quality_flags"].append("llm_processing_failed")
            return None, {
                "facts": None,
                "verification": {
                    "approved": False,
                    "unsupported_claims": [str(exc)],
                    "notes": "Falha na etapa de LLM.",
                },
            }

        return (
            {
                "input": {"problem_context": normalized_issue["problem_context"]},
                "output": {"canonical_answer": answer},
                "facts": facts,
                "model": self.llm_processor.model,
                "prompt_version": PROMPT_VERSION,
                "source_issue_key": normalized_issue["issue_key"],
            },
            {
                "facts": facts,
                "verification": verification,
            },
        )

    def _render_review_markdown(
        self,
        normalized_issue: dict[str, Any],
        gold_entry: dict[str, Any] | None,
        verification: dict[str, Any] | None,
    ) -> str:
        metadata = normalized_issue["metadata"]
        lines = [
            f"# {normalized_issue['issue_key']} - {normalized_issue['summary'] or 'Sem titulo'}",
            "",
            "## Metadados",
            "",
            f"- Status: {normalized_issue['status'] or 'N/A'}",
            f"- Responsavel: {normalized_issue['assignee'] or 'N/A'}",
            f"- Solicitante: {normalized_issue['reporter'] or 'N/A'}",
            f"- ERP do cliente: {metadata.get('erp_cliente') or 'N/A'}",
            f"- Assunto: {metadata.get('assunto') or 'N/A'}",
            f"- Natureza: {metadata.get('natureza') or 'N/A'}",
            f"- Atualizado em: {normalized_issue['updated'] or 'N/A'}",
            "",
            "## Contexto do Problema",
            "",
            normalized_issue["problem_context"] or "Sem contexto estruturado.",
            "",
            "## Comentarios do Gatekeeper",
            "",
        ]

        if normalized_issue["gatekeeper_comments"]:
            for index, comment in enumerate(normalized_issue["gatekeeper_comments"], start=1):
                lines.extend(
                    [
                        f"### {index}. {comment['created'] or 'Sem data'} | {comment['author'] or 'Sem autor'}",
                        "",
                        comment["clean_body"] or "Sem texto.",
                        "",
                    ]
                )
        else:
            lines.extend(["Nenhum comentario elegivel do assignee foi identificado.", ""])

        lines.extend(["## Resposta Canonica", ""])
        if gold_entry:
            lines.extend([gold_entry["output"]["canonical_answer"], ""])
        else:
            lines.extend(["Nao gerada.", ""])

        lines.extend(["## Qualidade", ""])
        lines.extend(
            [
                f"- Flags: {', '.join(normalized_issue['quality_flags']) or 'nenhuma'}",
                f"- Comentarios primarios: {', '.join(normalized_issue['primary_comment_ids']) or 'nenhum'}",
                f"- Secoes ausentes: {', '.join(normalized_issue['missing_context_sections']) or 'nenhuma'}",
            ]
        )

        if verification:
            lines.append(f"- Groundedness aprovado: {'sim' if verification.get('approved') else 'nao'}")
            if verification.get("unsupported_claims"):
                lines.append(f"- Afirmacoes sem suporte: {' | '.join(verification['unsupported_claims'])}")

        lines.append("")
        return "\n".join(lines).strip() + "\n"

    def run(
        self,
        *,
        jql: str = DEFAULT_JQL,
        full_refresh: bool = False,
        since_updated: str | None = None,
        limit: int | None = None,
    ) -> dict[str, Any]:
        self._prepare_output_dir(full_refresh=full_refresh)
        run_started_at = _utc_now_iso()
        since_dt = self._resolve_since_updated(since_updated=since_updated, full_refresh=full_refresh)
        effective_jql = build_incremental_jql(jql, since_dt)

        fields_payload = self.jira_client.fetch_fields()
        field_ids = discover_field_ids(fields_payload)
        _write_json(self.output_dir / "raw" / "fields.json", {"resolved_field_ids": field_ids, "fields": fields_payload})

        listed_issues = self.jira_client.search_issues(effective_jql, limit=limit, page_size=100)

        normalized_rows: list[dict[str, Any]] = []
        gold_rows: list[dict[str, Any]] = []
        review_rows: list[dict[str, Any]] = []
        last_processed_updated = ""
        last_processed_key = ""

        for base_issue in listed_issues:
            issue_key = _safe_strip(base_issue.get("key"))
            if not issue_key:
                continue
            issue_detail = self.jira_client.fetch_issue_detail(issue_key, field_ids)
            _write_json(self.output_dir / "raw" / "issues" / f"{issue_key}.json", issue_detail)

            normalized_issue = self._normalize_issue(issue_detail, field_ids)
            gold_entry, llm_meta = self._generate_gold(normalized_issue)

            verification = (llm_meta or {}).get("verification") or {"approved": False, "unsupported_claims": [], "notes": ""}
            grounded_approved = bool(verification.get("approved"))
            if gold_entry and not grounded_approved:
                normalized_issue["quality_flags"].append("grounding_failed")
                gold_entry = None

            confidence = calculate_confidence(
                context_sections=normalized_issue["context_sections"],
                substantive_comment_ids=normalized_issue["primary_comment_ids"],
                grounded_approved=grounded_approved,
                requires_attachment_review=normalized_issue["requires_attachment_review"],
                llm_used=not self.no_llm,
            )

            if confidence < self.review_threshold and "needs_review" not in normalized_issue["quality_flags"]:
                normalized_issue["quality_flags"].append("needs_review")

            confidence_below_threshold = confidence < self.review_threshold
            normalized_issue["confidence"] = confidence
            normalized_issue["review_reason"] = build_review_reason(
                normalized_issue["quality_flags"],
                normalized_issue["missing_context_sections"],
                grounded_approved,
                has_primary_comments=bool(normalized_issue["primary_comment_ids"]),
                confidence_below_threshold=confidence_below_threshold,
            )
            normalized_issue["llm"] = {
                "prompt_version": PROMPT_VERSION,
                "model": None if self.no_llm or self.llm_processor is None else self.llm_processor.model,
                "facts": (llm_meta or {}).get("facts"),
                "verification": verification,
            }

            review_markdown = self._render_review_markdown(normalized_issue, gold_entry, verification)
            review_md_path = self.output_dir / "review" / "markdown" / f"{issue_key}.md"
            review_md_path.write_text(review_markdown, encoding="utf-8")

            normalized_rows.append(normalized_issue)
            if gold_entry:
                gold_entry["confidence"] = confidence
                gold_rows.append(gold_entry)

            review_rows.append(
                {
                    "issue_key": issue_key,
                    "summary": normalized_issue["summary"],
                    "status": normalized_issue["status"],
                    "updated": normalized_issue["updated"],
                    "confidence": confidence,
                    "needs_review": "sim" if "needs_review" in normalized_issue["quality_flags"] else "nao",
                    "requires_attachment_review": "sim"
                    if "requires_attachment_review" in normalized_issue["quality_flags"]
                    else "nao",
                    "primary_comment_ids": ", ".join(normalized_issue["primary_comment_ids"]),
                    "missing_context_sections": ", ".join(normalized_issue["missing_context_sections"]),
                    "review_reason": normalized_issue["review_reason"],
                }
            )

            updated = normalized_issue["updated"]
            if updated:
                parsed_updated = _parse_datetime(updated)
                parsed_last = _parse_datetime(last_processed_updated) if last_processed_updated else None
                if not parsed_last or (parsed_updated is not None and parsed_updated >= parsed_last):
                    last_processed_updated = updated
                    last_processed_key = issue_key

        _write_jsonl(self.output_dir / "normalized" / "issues.jsonl", normalized_rows)
        _write_jsonl(self.output_dir / "gold" / "pairs.jsonl", gold_rows)

        review_csv_path = self.output_dir / "review" / "review.csv"
        review_csv_path.parent.mkdir(parents=True, exist_ok=True)
        with review_csv_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "issue_key",
                    "summary",
                    "status",
                    "updated",
                    "confidence",
                    "needs_review",
                    "requires_attachment_review",
                    "primary_comment_ids",
                    "missing_context_sections",
                    "review_reason",
                ],
            )
            writer.writeheader()
            writer.writerows(review_rows)

        review_zip_path = self.output_dir / "review" / "review_bundle.zip"
        with zipfile.ZipFile(review_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.write(review_csv_path, arcname="review.csv")
            for markdown_path in sorted((self.output_dir / "review" / "markdown").glob("*.md")):
                archive.write(markdown_path, arcname=f"markdown/{markdown_path.name}")

        manifest = {
            "generated_at": _utc_now_iso(),
            "run_started_at": run_started_at,
            "jql": jql,
            "effective_jql": effective_jql,
            "since_updated": since_dt.isoformat() if since_dt else "",
            "listed_issues": len(listed_issues),
            "normalized_issues": len(normalized_rows),
            "gold_pairs": len(gold_rows),
            "review_items": sum(1 for row in normalized_rows if "needs_review" in row["quality_flags"]),
            "field_ids": field_ids,
            "review_threshold": self.review_threshold,
            "prompt_version": PROMPT_VERSION,
            "llm_enabled": not self.no_llm,
            "last_processed_updated": last_processed_updated,
            "last_processed_key": last_processed_key,
        }
        _write_json(self.output_dir / "raw" / "manifest.json", manifest)
        self._save_checkpoint(
            {
                "last_updated": last_processed_updated,
                "last_key": last_processed_key,
                "generated_at": manifest["generated_at"],
                "prompt_version": PROMPT_VERSION,
            }
        )
        return manifest


def _require_jira_credentials() -> JiraCredentials:
    env_base_url = _safe_strip(os.getenv("JIRA_BASE_URL") or os.getenv("JIRA_URL"))
    env_username = _safe_strip(os.getenv("JIRA_USERNAME") or os.getenv("USERNAME"))
    env_password = _safe_strip(os.getenv("JIRA_PASSWORD") or os.getenv("PASSWORD"))
    env_api_token = _safe_strip(os.getenv("JIRA_API_TOKEN"))
    env_session_cookie = _safe_strip(os.getenv("JIRA_SESSION_COOKIE"))

    cfg_base_url = _safe_strip(getattr(config, "JIRA_BASE_URL", "") or getattr(config, "JIRA_URL", ""))
    cfg_username = _safe_strip(getattr(config, "JIRA_USERNAME", ""))
    cfg_password = _safe_strip(getattr(config, "JIRA_PASSWORD", ""))
    cfg_api_token = _safe_strip(getattr(config, "JIRA_API_TOKEN", ""))
    cfg_session_cookie = _safe_strip(getattr(config, "JIRA_SESSION_COOKIE", ""))

    base_url = env_base_url or cfg_base_url
    username = env_username or cfg_username or None
    session_cookie = env_session_cookie or cfg_session_cookie or None

    if env_api_token:
        api_token = env_api_token
        password = None
    elif env_password:
        api_token = None
        password = env_password
    else:
        api_token = cfg_api_token or None
        password = cfg_password or None

    if not base_url:
        raise EnvironmentError("JIRA_BASE_URL/JIRA_URL nao configurada.")
    if not ((username and (api_token or password)) or session_cookie):
        raise EnvironmentError(
            "Configure JIRA_USERNAME + JIRA_API_TOKEN, JIRA_USERNAME + JIRA_PASSWORD ou JIRA_SESSION_COOKIE para acessar o Jira."
        )

    timeout_raw = _safe_strip(
        getattr(config, "JIRA_REQUEST_TIMEOUT_SECONDS", os.getenv("JIRA_REQUEST_TIMEOUT_SECONDS", "60"))
    )
    timeout_seconds = float(timeout_raw or "60")
    return JiraCredentials(
        base_url=base_url,
        username=username,
        password=password,
        api_token=api_token,
        session_cookie=session_cookie,
        timeout_seconds=timeout_seconds,
    )


def validate_llm_runtime() -> None:
    provider = (config.LLM_PROVIDER or "gemini").strip().lower()
    if provider == "openai" and not config.OPENAI_API_KEY:
        raise EnvironmentError("OPENAI_API_KEY nao configurada para gerar a camada gold.")
    if provider == "gemini" and not config.GEMINI_API_KEY:
        raise EnvironmentError("GEMINI_API_KEY nao configurada para gerar a camada gold.")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extrai tickets Gatekeeper e gera dataset estruturado.")
    parser.add_argument("--jql", default=DEFAULT_JQL, help="JQL base para listar os tickets.")
    parser.add_argument("--full-refresh", action="store_true", help="Regera toda a estrutura de saida.")
    parser.add_argument("--since-updated", help="Data inicial para execucao incremental (ISO-8601 ou YYYY-MM-DD HH:MM).")
    parser.add_argument("--limit", type=int, help="Limite maximo de issues a processar.")
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Diretorio base de saida para raw/normalized/gold/review.",
    )
    parser.add_argument("--no-llm", action="store_true", help="Nao gera a camada gold nem roda verificador.")
    parser.add_argument(
        "--review-threshold",
        type=float,
        default=0.75,
        help="Limiar minimo de confianca para nao marcar o ticket como revisao.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    credentials = _require_jira_credentials()
    if not args.no_llm:
        validate_llm_runtime()

    jira_client = JiraApiClient(credentials)
    try:
        llm_processor = None if args.no_llm else GatekeeperLlmProcessor()
        pipeline = GatekeeperDatasetPipeline(
            jira_client=jira_client,
            output_dir=Path(args.output_dir),
            review_threshold=args.review_threshold,
            llm_processor=llm_processor,
            no_llm=args.no_llm,
            assignee_aliases=parse_assignee_aliases(
                getattr(config, "JIRA_ASSIGNEE_ALIASES", os.getenv("JIRA_ASSIGNEE_ALIASES"))
            ),
        )
        manifest = pipeline.run(
            jql=args.jql,
            full_refresh=args.full_refresh,
            since_updated=args.since_updated,
            limit=args.limit,
        )
    finally:
        jira_client.close()

    logger.info(
        "Pipeline finalizado: %s issues normalizadas, %s pares gold.",
        manifest["normalized_issues"],
        manifest["gold_pairs"],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
