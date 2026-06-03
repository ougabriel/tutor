@echo off
setlocal EnableExtensions
chcp 65001 >nul
title ExamTopics Scraper - Install Dependencies
color 0A

cd /d "%~dp0"

echo.
echo ============================================================
echo   ExamTopics Scraper - Dependency Installer
echo ============================================================
echo.

if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found.
    echo Run this file from the project folder.
    echo.
    pause
    exit /b 1
)

where py >nul 2>&1
if %ERRORLEVEL%==0 (
    set "PY_CMD=py -3"
) else (
    where python >nul 2>&1
    if errorlevel 1 (
        echo [ERROR] Python not found in PATH.
        echo Install Python 3, then run this file again.
        echo.
        pause
        exit /b 1
    )
    set "PY_CMD=python"
)

if not exist ".venv\Scripts\python.exe" (
    echo [1/4] Creating local virtual environment...
    %PY_CMD% -m venv .venv
    if errorlevel 1 goto failed
) else (
    echo [1/4] Local virtual environment already exists.
)

echo [2/4] Activating virtual environment...
call ".venv\Scripts\activate.bat"
if errorlevel 1 goto failed

echo [3/4] Installing Python packages...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 goto failed
python -m pip install -r requirements.txt
if errorlevel 1 goto failed

echo [4/4] Fetching Camoufox browser files...
python -m camoufox fetch
if errorlevel 1 goto failed

echo.
echo ============================================================
echo   Install complete.
echo   Next: double-click run_scraper.bat
echo ============================================================
echo.
pause
exit /b 0

:failed
echo.
echo ============================================================
echo   Install failed. Check error above.
echo ============================================================
echo.
pause
exit /b 1
