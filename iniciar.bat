@echo off
setlocal
title Bot Maxima - Discord
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo Virtualenv .venv nao encontrada.
    echo Execute setup_maquina.bat antes de iniciar o bot.
    echo.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat
echo.
echo  Iniciando Bot Discord...
echo  Pressione Ctrl+C para encerrar.
echo.
python bot.py
pause
