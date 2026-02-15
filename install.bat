@echo off
REM ARGUS Installation Script for Windows

echo.
echo ========================================
echo ARGUS Installation Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [*] Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [+] Installation complete!
echo.
echo Usage:
echo   python argus.py --help
echo   python argus.py network-scan --target 8.8.8.8
echo   python argus.py port-scan --target 8.8.8.8 --ports 80,443,8080
echo   python argus.py geoip --target 8.8.8.8 --output report.json
echo.
echo Environment variables (optional):
echo   ARGUS_LOG_FILE=custom.log
echo   ARGUS_GEOIP_API_KEY=your_key
echo   ARGUS_THREAT_INTEL_API_KEY=your_key
echo.
pause
