#!/bin/bash
# ARGUS Installation Script for Linux/macOS

echo ""
echo "========================================"
echo "ARGUS Installation Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.11+ from https://www.python.org/downloads/"
    exit 1
fi

echo "[*] Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[+] Installation complete!"
echo ""
echo "Usage:"
echo "  python3 argus.py --help"
echo "  python3 argus.py network-scan --target 8.8.8.8"
echo "  python3 argus.py port-scan --target 8.8.8.8 --ports 80,443,8080"
echo "  python3 argus.py geoip --target 8.8.8.8 --output report.json"
echo ""
echo "Environment variables (optional):"
echo "  ARGUS_LOG_FILE=custom.log"
echo "  ARGUS_GEOIP_API_KEY=your_key"
echo "  ARGUS_THREAT_INTEL_API_KEY=your_key"
echo ""
