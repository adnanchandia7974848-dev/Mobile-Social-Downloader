@echo off
cd /d "%~dp0"
title A Social Downloader Mobile App
echo Starting A Social Downloader App...
"D:\Extentions\A Downloader\python_env\python.exe" main.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Application exited with an error. Press any key to close...
    pause >nul
)
