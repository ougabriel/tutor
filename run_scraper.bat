@echo off
setlocal EnableExtensions
chcp 65001 >nul
title ExamTopics Scraper
color 0B

cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    set "PYTHON_EXE=.venv\Scripts\python.exe"
) else (
    echo [WARN] Local .venv not found.
    echo Run install_dependencies.bat first for best results.
    echo.
    where python >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python not found.
        echo.
        pause
        exit /b 1
    )
    set "PYTHON_EXE=python"
)

%PYTHON_EXE% main.py

echo.
echo ============================================================
echo   Finished.
echo ============================================================
echo.
pause
exit /b 0
