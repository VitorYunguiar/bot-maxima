"""
Gera o pacote do Microsoft Teams a partir do .env.

Uso:
    .\.venv\Scripts\python.exe scripts\build_teams_package.py
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import config

TEAMS_DIR = ROOT_DIR / "teams_manifest"
BUILD_DIR = TEAMS_DIR / "build"
TEMPLATE_PATH = TEAMS_DIR / "manifest.template.json"
COLOR_ICON_PATH = TEAMS_DIR / "color.png"
OUTLINE_ICON_PATH = TEAMS_DIR / "outline.png"
MANIFEST_OUTPUT_PATH = BUILD_DIR / "manifest.json"
ZIP_OUTPUT_PATH = BUILD_DIR / "bot-azure.zip"


def _replace_placeholders(value, replacements: dict[str, str]):
    if isinstance(value, dict):
        return {key: _replace_placeholders(item, replacements) for key, item in value.items()}
    if isinstance(value, list):
        return [_replace_placeholders(item, replacements) for item in value]
    if isinstance(value, str) and value.startswith("__") and value.endswith("__"):
        placeholder = value[2:-2]
        if placeholder not in replacements:
            raise KeyError(f"Placeholder sem valor no template do Teams: {placeholder}")
        return replacements[placeholder]
    return value


def _assert_required_files():
    missing = [str(path) for path in (TEMPLATE_PATH, COLOR_ICON_PATH, OUTLINE_ICON_PATH) if not path.exists()]
    if missing:
        raise FileNotFoundError(
            "Arquivos obrigatorios do pacote do Teams nao encontrados: " + ", ".join(missing)
        )


def build_teams_package() -> dict[str, Path]:
    """Gera manifest.json e bot-azure.zip em teams_manifest/build."""
    config.validate_teams_manifest()
    _assert_required_files()

    replacements = config.get_teams_manifest_context()
    template_data = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))
    manifest_data = _replace_placeholders(template_data, replacements)

    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_OUTPUT_PATH.write_text(
        json.dumps(manifest_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    color_output = BUILD_DIR / COLOR_ICON_PATH.name
    outline_output = BUILD_DIR / OUTLINE_ICON_PATH.name
    color_output.write_bytes(COLOR_ICON_PATH.read_bytes())
    outline_output.write_bytes(OUTLINE_ICON_PATH.read_bytes())

    with zipfile.ZipFile(ZIP_OUTPUT_PATH, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(MANIFEST_OUTPUT_PATH, arcname="manifest.json")
        archive.write(color_output, arcname=color_output.name)
        archive.write(outline_output, arcname=outline_output.name)

    return {
        "build_dir": BUILD_DIR,
        "manifest_path": MANIFEST_OUTPUT_PATH,
        "zip_path": ZIP_OUTPUT_PATH,
    }


def main() -> int:
    try:
        outputs = build_teams_package()
    except Exception as exc:
        print(f"Erro ao gerar pacote do Teams: {exc}")
        return 1

    print(f"Manifesto gerado em: {outputs['manifest_path']}")
    print(f"Pacote gerado em: {outputs['zip_path']}")
    print(f"Diretorio de saida: {outputs['build_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
