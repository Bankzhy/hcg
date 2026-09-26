@echo off
setlocal
cd /d "%~dp0"

where py >nul 2>nul
if %errorlevel% equ 0 (
  py -3 serve.py %*
  exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel% equ 0 (
  python serve.py %*
  exit /b %errorlevel%
)

echo Python 3 is required to run HCG.
exit /b 1
