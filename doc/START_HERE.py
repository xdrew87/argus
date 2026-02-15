"""
ARGUS Framework - Quick Start Guide
Run this first before using ARGUS
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║                    ARGUS - QUICK START                         ║
║     Advanced Security Intelligence Platform v1.0               ║
╚════════════════════════════════════════════════════════════════╝

📋 PROJECT STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CLI/
├── argus.py              ← Main entry point
├── config.py             ← Configuration constants
├── demo.py               ← Demo/test script (no deps required)
├── requirements.txt      ← Python dependencies
├── README.md             ← Full documentation
├── install.bat           ← Windows installer
├── install.sh            ← Linux/macOS installer
├── .gitignore
│
├── core/
│   ├── ui.py             ← Terminal UI & formatting
│   ├── logging.py        ← Logging system
│   ├── utils.py          ← Input validation & helpers
│   └── plugin_loader.py  ← Plugin auto-loader
│
├── modules/
│   ├── network_scanner.py    ← Network reachability checks
│   ├── port_scanner.py       ← Threaded port scanning
│   ├── breach_checker.py     ← Breach intelligence 
│   ├── ssl_monitor.py        ← SSL/TLS certificate checks
│   ├── geoip_lookup.py       ← GeoIP & ISP data
│   ├── threat_intel.py       ← Threat enrichment
│   └── audit_report.py       ← Report generation
│
└── plugins/              ← Auto-loaded external modules


🔧 INSTALLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Windows:
  1. install.bat (automatic)
  OR
  2. pip install -r requirements.txt

Linux/macOS:
  1. chmod +x install.sh
  2. ./install.sh
  OR
  3. pip3 install -r requirements.txt


📦 DEPENDENCIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✓ colorama>=0.4.6       (Terminal colors)
  ✓ requests>=2.31.0      (HTTP library)
  ✓ Python 3.11+          (Built-in: socket, ssl, subprocess, etc.)


🚀 RUNNING ARGUS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Show Help:
  python argus.py --help

Available Modules:
  • network-scan    - Check if host is reachable
  • port-scan       - Scan open ports (threaded)
  • breach-check    - Check for known breaches
  • ssl-monitor     - Check SSL certificate status
  • geoip           - Get geographic & ISP info
  • threat-intel    - Get threat intelligence
  • audit-report    - Generate audit report

Examples:

  # Network scan
  python argus.py network-scan --target 8.8.8.8

  # Port scan (default: 22,80,443,8080)
  python argus.py port-scan --target 8.8.8.8

  # Port scan with custom ports
  python argus.py port-scan --target 8.8.8.8 --ports 22,80,443,3306,5432

  # GeoIP lookup with JSON output
  python argus.py geoip --target 1.1.1.1 --output report.json

  # SSL certificate check
  python argus.py ssl-monitor --target google.com

  # Verbose logging
  python argus.py network-scan --target 8.8.8.8 --verbose


🧪 TESTING (NO DEPENDENCIES REQUIRED)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Run demo with input validation & network tests:
  python demo.py

This tests:
  ✓ IP address validation
  ✓ Hostname resolution
  ✓ Port validation
  ✓ Network scanner
  ✓ Port scanner
  ✓ UI components
  (No external dependencies or API keys required!)


🔑 ENVIRONMENT VARIABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Windows (Command Prompt):
  set ARGUS_LOG_FILE=custom.log
  set ARGUS_GEOIP_API_KEY=your_key_here
  set ARGUS_THREAT_INTEL_API_KEY=your_key_here
  python argus.py ...

Windows (PowerShell):
  $env:ARGUS_LOG_FILE="custom.log"
  $env:ARGUS_GEOIP_API_KEY="your_key_here"
  python argus.py ...

Linux/macOS:
  export ARGUS_LOG_FILE=custom.log
  export ARGUS_GEOIP_API_KEY=your_key_here
  python3 argus.py ...


📊 OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Console Output:
  • Boxed ANSI formatted results
  • Color-coded status (success/warning/error)
  • Live logging to console

Log File:
  • argus.log (default, customizable)
  • Timestamps, levels, and messages
  • Persistent audit trail

JSON Reports:
  • Export scan results with --output flag
  • Machine-readable format
  • Integration-ready


🛡️ SECURITY NOTES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ NO hardcoded secrets/API keys
✓ Environment variable based configuration
✓ Input validation on all targets
✓ Secure error handling (no sensitive leaks)
✓ Proper exception handling (no bare except)
✓ HTTPS/secure protocol enforcement
✓ Cross-platform compatible

⚠️  ETHICAL USE ONLY - Defensive/Analytical purposes


❓ TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"ImportError: No module named 'requests'"
  → Run: pip install -r requirements.txt

"Permission denied" on install.sh
  → Run: chmod +x install.sh

Port scan timeout
  → Increase timeout in config.py or use fewer ports

No GeoIP results
  → Check internet connection and valid target IP

Can't resolve hostname
  → Verify hostname is correct and DNS working


📚 MODULES OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

network_scanner.py
  • Ping/ICMP checks
  • Host reachability
  • Returns: {target, reachable}

port_scanner.py
  • ThreadPoolExecutor (10 workers)
  • Socket-based port detection
  • Returns: {target, ports: [{port, open},...]}

ssl_monitor.py
  • SSL/TLS certificate validation
  • Certificate details extraction
  • Returns: {target, port, ssl_status, certificate}

geoip_lookup.py
  • Uses suicixde.com API (free, no key required)
  • Geo, ISP, threat level, timezone
  • Returns full GeoIP data

breach_checker.py
  • Breach database lookup
  • Requires API key in environment
  • Returns: {target, breach_data}

threat_intel.py
  • Threat enrichment data
  • Requires API key in environment  
  • Returns: {target, threat_intel_data}

audit_report.py
  • Summary report generation
  • Aggregates scan results
  • Returns readable audit output


🎯 QUICK EXAMPLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Scan Google's public DNS:
  python argus.py port-scan --target 8.8.8.8 --ports 53,80,443

Check your own server:
  python argus.py network-scan --target 192.168.1.1 --verbose

Full audit export:
  python argus.py audit-report --target example.com --output audit.json

GeoIP + JSON:
  python argus.py geoip --target 1.1.1.1 --output geoip.json


✅ EVERYTHING FIXED!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Core modules (ui, logging, utils, plugin_loader)
✓ All 7 security modules complete
✓ Main entry point (argus.py)
✓ Configuration management (config.py)
✓ Demo/testing script (demo.py)
✓ Installation scripts (install.bat, install.sh)
✓ Documentation (README.md)
✓ .gitignore for version control
✓ Production-ready error handling
✓ Secure coding practices

Ready to use!
""")
