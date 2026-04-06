@echo off
setlocal
title Gerar Pacote Teams
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo Virtualenv .venv nao encontrada.
    echo Crie ou atualize a .venv antes de gerar o pacote do Teams.
    echo.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat

.\.venv\Scripts\python.exe scripts\build_teams_package.py
if errorlevel 1 (
    echo.
    pause
    exit /b 1
)

echo.
echo Pacote do Teams disponivel em teams_manifest\build\
echo.
pause
