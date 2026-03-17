@echo off
title Bot Maxima - Discord
cd /d "%~dp0"
call .venv\Scripts\activate.bat
echo.
echo  Iniciando Bot Discord...
echo  Pressione Ctrl+C para encerrar.
echo.
python bot.py
pause
