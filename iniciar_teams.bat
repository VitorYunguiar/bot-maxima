@echo off
setlocal
title Bot Maxima - Teams
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo Virtualenv .venv nao encontrada.
    echo Crie ou atualize a .venv antes de iniciar o bot do Teams.
    echo.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat

.\.venv\Scripts\python.exe scripts\check_teams_runtime.py
if errorlevel 1 (
    echo.
    pause
    exit /b 1
)

echo.
echo  Iniciando Bot Teams...
echo  Pressione Ctrl+C para encerrar.
echo.
python bot_teams.py
pause
