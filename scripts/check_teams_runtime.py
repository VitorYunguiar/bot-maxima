"""
Valida dependencias minimas para subir o bot do Microsoft Teams.
"""

from __future__ import annotations

import importlib.util


def _has_module(module_name: str) -> bool:
    try:
        return importlib.util.find_spec(module_name) is not None
    except ModuleNotFoundError:
        return False


def main() -> int:
    missing = []

    if not _has_module("dotenv"):
        missing.append("python-dotenv")
    if not _has_module("aiohttp"):
        missing.append("aiohttp")
    if not _has_module("botbuilder.core") or not _has_module("botbuilder.integration.aiohttp"):
        missing.append("botbuilder")

    if missing:
        print("Dependencias obrigatorias do Teams nao encontradas na .venv: " + ", ".join(missing))
        print("Instale com: .\\.venv\\Scripts\\python.exe -m pip install -r requirements.txt")
        return 1

    print("Dependencias do Teams verificadas com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
