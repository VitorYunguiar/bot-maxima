@echo off
setlocal
cd /d "%~dp0"

where pyw >nul 2>nul
if %errorlevel%==0 (
    start "" pyw scripts\gatekeeper_export_gui.py
) else (
    py scripts\gatekeeper_export_gui.py
)
