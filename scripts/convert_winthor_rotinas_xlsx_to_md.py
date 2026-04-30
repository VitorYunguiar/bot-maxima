"""
Converte uma planilha XLSX de rotinas x tabelas do WinThor para um markdown
estruturado para ingestao no RAG local.

Nao depende de openpyxl; le o XLSX diretamente via ZIP + XML.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


MAIN_NS = {"a": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
REL_NS = {"r": "http://schemas.openxmlformats.org/package/2006/relationships"}
CELL_REF_RE = re.compile(r"([A-Z]+)")
TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9_]*(?:\.[A-Z][A-Z0-9_]*)?\b")
TABLE_TOKEN_ALLOWLIST = {"PACKAGES", "FUNCOES", "FUNCTIONS", "PROCEDURES", "TRIGGERS", "VIEWS"}
MISSING_LABEL = "Nao informado na planilha"


@dataclass(frozen=True)
class RoutineEntry:
    row_number: int
    rotina: str
    nome: str
    modulo: str | None
    tabela_raw: str | None
    observacoes: str | None

    @property
    def modulo_display(self) -> str:
        return self.modulo or MISSING_LABEL

    @property
    def tabela_display(self) -> str:
        return self.tabela_raw or MISSING_LABEL


def _clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    text = re.sub(r"\s+", " ", value).strip()
    return text or None


def _ascii_slug(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    ascii_text = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text.lower()).strip("-")
    return ascii_text or "documento"


def _split_path_target(target: str) -> str:
    clean_target = target.replace("\\", "/")
    if clean_target.startswith("/"):
        clean_target = clean_target[1:]
    return clean_target


def _read_shared_strings(archive: zipfile.ZipFile) -> list[str]:
    if "xl/sharedStrings.xml" not in archive.namelist():
        return []
    root = ET.fromstring(archive.read("xl/sharedStrings.xml"))
    values: list[str] = []
    for item in root.findall("a:si", MAIN_NS):
        text = "".join(node.text or "" for node in item.iterfind(".//a:t", MAIN_NS))
        values.append(text)
    return values


def _resolve_sheet_path(archive: zipfile.ZipFile, sheet_name: str | None) -> tuple[str, str]:
    workbook = ET.fromstring(archive.read("xl/workbook.xml"))
    rels = ET.fromstring(archive.read("xl/_rels/workbook.xml.rels"))
    rel_map = {
        rel.attrib["Id"]: rel.attrib["Target"]
        for rel in rels.findall("r:Relationship", REL_NS)
    }

    sheets = workbook.findall(".//a:sheets/a:sheet", MAIN_NS)
    if not sheets:
        raise ValueError("A planilha nao possui abas.")

    target_sheet = None
    if sheet_name:
        for sheet in sheets:
            if (sheet.attrib.get("name") or "").strip().lower() == sheet_name.strip().lower():
                target_sheet = sheet
                break
        if target_sheet is None:
            available = ", ".join(sheet.attrib.get("name", "") for sheet in sheets)
            raise ValueError(f"Aba '{sheet_name}' nao encontrada. Abas disponiveis: {available}")
    else:
        target_sheet = sheets[0]

    rel_id = target_sheet.attrib.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
    if not rel_id or rel_id not in rel_map:
        raise ValueError("Nao foi possivel localizar o XML da aba selecionada.")

    return target_sheet.attrib.get("name", "Planilha"), f"xl/{_split_path_target(rel_map[rel_id])}"


def _cell_value(cell: ET.Element, shared_strings: list[str]) -> str | None:
    cell_type = cell.attrib.get("t")
    value_node = cell.find("a:v", MAIN_NS)
    inline_node = cell.find("a:is", MAIN_NS)

    if cell_type == "s" and value_node is not None and value_node.text is not None:
        return shared_strings[int(value_node.text)]
    if cell_type == "inlineStr" and inline_node is not None:
        return "".join(node.text or "" for node in inline_node.iterfind(".//a:t", MAIN_NS))
    if value_node is not None:
        return value_node.text
    return None


def _iter_sheet_rows(
    archive: zipfile.ZipFile,
    sheet_path: str,
    shared_strings: list[str],
) -> list[tuple[int, dict[str, str | None]]]:
    sheet_root = ET.fromstring(archive.read(sheet_path))
    rows: list[tuple[int, dict[str, str | None]]] = []
    for row in sheet_root.findall(".//a:sheetData/a:row", MAIN_NS):
        row_number = int(row.attrib.get("r", "0"))
        values: dict[str, str | None] = {}
        for cell in row.findall("a:c", MAIN_NS):
            ref = cell.attrib.get("r", "")
            match = CELL_REF_RE.match(ref)
            if not match:
                continue
            values[match.group(1)] = _clean_text(_cell_value(cell, shared_strings))
        rows.append((row_number, values))
    return rows


def load_entries(xlsx_path: Path, sheet_name: str | None = None) -> tuple[str, list[RoutineEntry]]:
    with zipfile.ZipFile(xlsx_path) as archive:
        shared_strings = _read_shared_strings(archive)
        resolved_sheet_name, sheet_path = _resolve_sheet_path(archive, sheet_name)
        sheet_rows = _iter_sheet_rows(archive, sheet_path, shared_strings)

    if not sheet_rows:
        raise ValueError("A planilha esta vazia.")

    header_row_number, header_cells = sheet_rows[0]
    header_map = {col: value for col, value in header_cells.items() if value}
    if not header_map:
        raise ValueError(f"Nao foi possivel ler o cabecalho da linha {header_row_number}.")

    reverse_header_map = {name.lower(): col for col, name in header_map.items()}
    required_headers = ["rotina", "nome", "modulo", "tabela", "observações"]
    if "observações" not in reverse_header_map and "observacoes" in reverse_header_map:
        reverse_header_map["observações"] = reverse_header_map["observacoes"]

    missing_headers = [name for name in required_headers if name not in reverse_header_map]
    if missing_headers:
        raise ValueError(f"Cabecalho ausente na planilha: {', '.join(missing_headers)}")

    entries: list[RoutineEntry] = []
    for row_number, row_cells in sheet_rows[1:]:
        row_values = {header_map[col]: value for col, value in row_cells.items() if col in header_map}
        if not any(row_values.values()):
            continue
        entry = RoutineEntry(
            row_number=row_number,
            rotina=row_values.get("Rotina") or "",
            nome=row_values.get("Nome") or "",
            modulo=row_values.get("Modulo"),
            tabela_raw=row_values.get("Tabela"),
            observacoes=row_values.get("Observações") or row_values.get("Observacoes"),
        )
        if not entry.rotina and not entry.nome:
            continue
        entries.append(entry)

    return resolved_sheet_name, entries


def extract_table_tokens(table_value: str | None) -> list[str]:
    if not table_value:
        return []
    upper_value = unicodedata.normalize("NFKD", table_value).encode("ascii", "ignore").decode("ascii").upper()
    tokens: list[str] = []
    seen: set[str] = set()
    for match in TOKEN_RE.finditer(upper_value):
        token = match.group(0)
        if len(token) < 3:
            continue
        if not (
            token.startswith(("PC", "MXS", "ERP", "FUNC", "SYNC"))
            or "_" in token
            or "." in token
            or token in TABLE_TOKEN_ALLOWLIST
        ):
            continue
        if token in seen:
            continue
        seen.add(token)
        tokens.append(token)
    return tokens


def _numeric_sort_key(value: str) -> tuple[int, str]:
    value = value.strip()
    if value.isdigit():
        return int(value), value
    digits = re.sub(r"\D+", "", value)
    if digits:
        return int(digits), value
    return 999999999, value


def _format_inline_code_list(values: list[str]) -> str:
    if not values:
        return MISSING_LABEL
    return ", ".join(f"`{value}`" for value in values)


def _keyword_line(entries: list[RoutineEntry], max_keywords: int = 18) -> str:
    counter: Counter[str] = Counter()
    for entry in entries:
        counter.update(extract_table_tokens(entry.tabela_raw))
    base_keywords = [
        "WinThor",
        "rotina",
        "tabela",
        "modulo",
        "consulta operacional",
        "consulta tecnica",
    ]
    for token, _count in counter.most_common(max(0, max_keywords - len(base_keywords))):
        if token not in base_keywords:
            base_keywords.append(token)
    return ", ".join(base_keywords[:max_keywords])


def render_markdown(
    *,
    source_path: Path,
    sheet_name: str,
    entries: list[RoutineEntry],
    title: str,
) -> str:
    sorted_entries = sorted(entries, key=lambda entry: (_numeric_sort_key(entry.rotina), entry.nome.lower()))
    by_module: dict[str, list[RoutineEntry]] = defaultdict(list)
    by_table: dict[str, list[RoutineEntry]] = defaultdict(list)

    for entry in sorted_entries:
        by_module[entry.modulo_display].append(entry)
        for token in extract_table_tokens(entry.tabela_raw):
            by_table[token].append(entry)

    missing_module_entries = [entry for entry in sorted_entries if not entry.modulo]
    missing_table_entries = [entry for entry in sorted_entries if not entry.tabela_raw]
    entries_with_notes = [entry for entry in sorted_entries if entry.observacoes]
    duplicated_routines = sorted(
        rotina for rotina, count in Counter(entry.rotina for entry in sorted_entries).items() if count > 1
    )

    lines: list[str] = [
        f"# {title}",
        "",
        f"**Palavras-chave**: {_keyword_line(sorted_entries)}",
        "",
        "**Sistema**: WinThor",
        "",
        "**Area**: Referencia operacional de rotinas e tabelas",
        "",
        "---",
        "",
        "## Visao geral",
        "",
        "Este documento foi normalizado a partir de uma planilha XLSX para uso no RAG deste ambiente.",
        "Cada rotina virou uma secao independente, com indices reversos por referencia tecnica e por modulo para melhorar recuperacao por embeddings e full-text search.",
        "",
        f"- Fonte original: `{source_path}`",
        f"- Aba utilizada: `{sheet_name}`",
        f"- Registros uteis convertidos: `{len(sorted_entries)}`",
        f"- Registros sem modulo informado: `{len(missing_module_entries)}`",
        f"- Registros sem tabela informada: `{len(missing_table_entries)}`",
        f"- Registros com observacoes: `{len(entries_with_notes)}`",
        f"- Rotinas repetidas na fonte: `{', '.join(duplicated_routines) if duplicated_routines else 'nenhuma'}`",
        "",
        "## Criterios de normalizacao",
        "",
        "- Campos vazios foram preservados como `Nao informado na planilha`.",
        "- O texto das tabelas foi mantido como veio na fonte e tambem tokenizado para busca reversa.",
        "- Quando uma rotina aparece mais de uma vez, cada linha foi preservada como um registro proprio.",
        "- Nao houve correcao semantica manual dos dados da planilha; o documento prioriza fidelidade a fonte.",
        "",
        "## Indice por rotina",
        "",
    ]

    for entry in sorted_entries:
        table_tokens = extract_table_tokens(entry.tabela_raw)
        lines.extend(
            [
                f"### Rotina {entry.rotina} - {entry.nome}",
                "",
                f"- Modulo WinThor: `{entry.modulo_display}`",
                f"- Referencia tecnica na planilha: `{entry.tabela_display}`",
                f"- Tabelas e tokens tecnicos normalizados para busca: {_format_inline_code_list(table_tokens)}",
                f"- Observacoes: `{entry.observacoes or MISSING_LABEL}`",
                f"- Linha original na planilha: `{entry.row_number}`",
                "",
                (
                    f"Resumo: a rotina `{entry.rotina}` ({entry.nome}) esta associada ao modulo "
                    f"`{entry.modulo_display}` e referencia `{entry.tabela_display}`."
                ),
                "",
            ]
        )

    lines.extend(
        [
            "## Indice reverso por referencia tecnica",
            "",
        ]
    )

    for table_name in sorted(by_table):
        related_entries = sorted(
            by_table[table_name],
            key=lambda entry: (_numeric_sort_key(entry.rotina), entry.nome.lower()),
        )
        module_names = sorted({entry.modulo_display for entry in related_entries})
        original_refs = sorted({entry.tabela_display for entry in related_entries})
        routines_label = "; ".join(f"`{entry.rotina} - {entry.nome}`" for entry in related_entries)
        lines.extend(
            [
                f"### Referencia tecnica {table_name}",
                "",
                f"- Rotinas relacionadas: {routines_label}",
                f"- Modulos relacionados: {_format_inline_code_list(module_names)}",
                f"- Referencias originais da planilha: {_format_inline_code_list(original_refs)}",
                "",
                (
                    f"Resumo: a referencia tecnica `{table_name}` aparece nas rotinas "
                    f"{', '.join(entry.rotina for entry in related_entries)}."
                ),
                "",
            ]
        )

    lines.extend(
        [
            "## Indice por modulo",
            "",
        ]
    )

    for module_name in sorted(by_module, key=lambda value: value.lower()):
        related_entries = sorted(
            by_module[module_name],
            key=lambda entry: (_numeric_sort_key(entry.rotina), entry.nome.lower()),
        )
        routines_label = "; ".join(f"`{entry.rotina} - {entry.nome}`" for entry in related_entries)
        related_tables = sorted({token for entry in related_entries for token in extract_table_tokens(entry.tabela_raw)})
        lines.extend(
            [
                f"### Modulo {module_name}",
                "",
                f"- Rotinas do modulo: {routines_label}",
                f"- Principais tabelas do modulo: {_format_inline_code_list(related_tables[:24])}",
                f"- Total de rotinas mapeadas neste modulo: `{len(related_entries)}`",
                "",
            ]
        )

    if missing_module_entries or missing_table_entries:
        lines.extend(
            [
                "## Pontos de atencao da fonte",
                "",
            ]
        )

        if missing_module_entries:
            missing_module_label = "; ".join(
                f"`{entry.rotina} - {entry.nome}`" for entry in missing_module_entries
            )
            lines.append(f"- Rotinas sem modulo informado: {missing_module_label}")

        if missing_table_entries:
            missing_table_label = "; ".join(
                f"`{entry.rotina} - {entry.nome}`" for entry in missing_table_entries
            )
            lines.append(f"- Rotinas sem tabela informada: {missing_table_label}")

        lines.extend(["", "## Fonte", "", "Documento gerado automaticamente a partir da planilha XLSX original."])
    else:
        lines.extend(["## Fonte", "", "Documento gerado automaticamente a partir da planilha XLSX original."])

    return "\n".join(lines).strip() + "\n"


def build_default_output_name(source_path: Path) -> str:
    stem = _ascii_slug(source_path.stem)
    return f"14-{stem}.md"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Converte uma planilha de rotinas x tabelas do WinThor em markdown para o RAG."
    )
    parser.add_argument("input", help="Caminho do arquivo XLSX de origem.")
    parser.add_argument(
        "--sheet",
        default=None,
        help="Nome da aba a ser convertida. Padrao: primeira aba.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Caminho do markdown de saida. Padrao: documentos/14-<nome-do-arquivo>.md",
    )
    parser.add_argument(
        "--title",
        default="WinThor - Rotinas x Tabelas",
        help="Titulo principal do documento markdown.",
    )
    args = parser.parse_args()

    root_dir = Path(__file__).resolve().parents[1]
    input_path = Path(args.input).expanduser().resolve()
    if not input_path.exists():
        raise FileNotFoundError(f"Arquivo XLSX nao encontrado: {input_path}")

    output_path = (
        Path(args.output).expanduser().resolve()
        if args.output
        else (root_dir / "documentos" / build_default_output_name(input_path)).resolve()
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    sheet_name, entries = load_entries(input_path, args.sheet)
    markdown = render_markdown(
        source_path=input_path,
        sheet_name=sheet_name,
        entries=entries,
        title=args.title,
    )
    output_path.write_text(markdown, encoding="utf-8")

    print(f"Arquivo de entrada: {input_path}")
    print(f"Aba convertida: {sheet_name}")
    print(f"Registros convertidos: {len(entries)}")
    print(f"Markdown gerado em: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
