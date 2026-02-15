# 🛡️ ARGUS - Advanced Security Intelligence Platform

[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Proprietary-red)](#license)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-brightgreen)](#cross-platform)

A modular, production-quality cybersecurity CLI framework for security analysis, monitoring, and reporting.

> **Note**: ARGUS is a defensive and analytical platform for visibility, monitoring, and reporting — not exploitation tooling.

## ✨ Features

- 🔍 **7 Security Modules** - Network scanning, port detection, SSL monitoring, GeoIP lookup, and more
- ⚡ **Threaded Port Scanning** - Fast concurrent scanning using ThreadPoolExecutor (10 workers)
- 🏗️ **Modular Architecture** - Clean separation of concerns with reusable core components
- 📊 **JSON Export** - Machine-readable reports for integration
- 📝 **Comprehensive Logging** - Dual file + console output with configurable levels
- 🔐 **Secure Configuration** - Environment variable-based API key management
- 🔌 **Plugin System** - Auto-load external modules from `plugins/` directory
- 🎨 **Rich Terminal UI** - ANSI colors, boxed formatting, and structured output
- ✅ **Production-Ready** - Error handling, input validation, secure coding practices
- 🌍 **Cross-Platform** - Windows, Linux, macOS compatible

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Installation

**Windows:**
```bash
install.bat
```

**Linux/macOS:**
```bash
chmod +x install.sh
./install.sh
```

**Manual:**
```bash
pip install -r requirements.txt
```

### Basic Usage

**Interactive Menu Mode (Recommended):**
```bash
python argus.py
```
This launches the interactive menu where you can:
- Select modules by number
- Enter target IP/hostname
- Configure ports (for port scanning)
- Export results to JSON
- Navigate with prompts

**Command-Line Mode:**
```bash
# Display help
python argus.py --help

# Network scan
python argus.py network-scan --target 8.8.8.8

# Port scan (default: 22,80,443,8080)
python argus.py port-scan --target 8.8.8.8

# Port scan with custom ports
python argus.py port-scan --target 8.8.8.8 --ports 22,80,443,3306,5432

# GeoIP lookup with JSON export
python argus.py geoip --target 1.1.1.1 --output report.json

# SSL certificate check
python argus.py ssl-monitor --target google.com

# Verbose logging
python argus.py network-scan --target 8.8.8.8 --verbose
```

## Available Modules

| Module | Command | Description |
|--------|---------|-------------|
| 🌐 Network Scanner | `network-scan` | Ping/ICMP reachability checks |
| 🔌 Port Scanner | `port-scan` | Threaded concurrent port scanning (10 workers) |
| 🔒 SSL Monitor | `ssl-monitor` | SSL/TLS certificate validation and expiry |
| 🌍 GeoIP Lookup | `geoip` | Geographic location & ISP information |
| 🚨 Breach Checker | `breach-check` | Known breach database lookup |
| ⚠️ Threat Intel | `threat-intel` | Threat intelligence enrichment |
| 📋 Audit Report | `audit-report` | Security audit report generation |

## 🔧 Configuration

### Environment Variables

For secure API key and configuration management:

**Windows (Command Prompt):**
```batch
set ARGUS_LOG_FILE=custom.log
set ARGUS_GEOIP_API_KEY=your_key_here
set ARGUS_THREAT_INTEL_API_KEY=your_key_here
python argus.py ...
```

**Windows (PowerShell):**
```powershell
$env:ARGUS_LOG_FILE="custom.log"
$env:ARGUS_GEOIP_API_KEY="your_key_here"
python argus.py ...
```

**Linux/macOS:**
```bash
export ARGUS_LOG_FILE=custom.log
export ARGUS_GEOIP_API_KEY=your_key_here
export ARGUS_THREAT_INTEL_API_KEY=your_key_here
python3 argus.py ...
```📁 Project Structure

```
CLI/
├── argus.py                 # Main CLI entry point
├── config.py                # Configuration & constants
├── demo.py                  # Demo script (no dependencies)
├── requirements.txt         # Python dependencies
├── install.bat / .sh        # Installation scripts
├── PROJECT_STRUCTURE.md     # Detailed structure
│
├── core/                    # Core framework modules
│   ├── ui.py                # Terminal UI & boxed formatting
│   ├── logging.py           # Logging system (file + console)
│   ├── utils.py             # Input validation & helpers
│   └── plugin_loader.py     # Plugin auto-loader
│
├── modules/                 # Security & scanning modules
│   ├── network_scanner.py   # Network reachability checks
│   ├── port_scanner.py      # Threaded port scanning
│   ├── breach_checker.py    # Breach database integration
│   ├── ssl_monitor.py       # SSL/TLS certificate checks
│   ├── geoip_lookup.py      # GeoIP geolocation lookup
│   ├── threat_intel.py      # Threat intelligence
│   └── audit_report.py      # Audit report generation
│
├── plugins/                 # External plugins (auto-loaded)
│💡 Design Philosophy

ARGUS is a **defensive and analytical platform** focused on:
- **Visibility** - Understanding the security landscape
- **Monitoring** - Continuous observation of security posture
- **Reporting** - Actionable security intelligence
- **Compliance** - Audit trails and structured reporting

**NOT** for exploitation or unauthorized access.

## 🧪 Testing

No dependencies required for basic testing:

```bash
python demo.py
```

This tests:
- ✅ IP address validation
- ✅ Hostname resolution
- ✅ Port validation
- ✅ Network scanning
- ✅ Port scanning
- ✅ UI components

## 📚 Documentation

For detailed information, see:
- [doc/README.md](doc/README.md) - Full documentation & usage guide
- [doc/START_HERE.py](doc/START_HERE.py) - Interactive quick start guide
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - Project structure overview

## 🔒 Security

This project follows secure coding practices:

- ✅ No hardcoded secrets or API keys
- ✅ Environment variable-based configuration
- ✅ Secure error handling (no bare `except`)
- ✅ Input validation on all targets
- ✅ Proper exception handling
- ✅ HTTPS for all API calls
- ✅ Responsible logging (no sensitive data leaks)

### ⚠️ Ethical Usage

- Only scan targets you own or have explicit permission to scan
- Follow all applicable laws and regulations
- Use for legitimate security/analytical purposes only
- Inform targets of scanning activities where appropriate

## 🛠️ Development Standards

- Python 3.11+
- PEP 8 compliant
- Full docstrings on all classes and functions
- Environment-based secret management
- Cross-platform compatibility
- Production-quality error handling
- Comprehensive logging

## 🤝 Contributing

### Adding New Modules

1. Create new file in `modules/` directory
2. Follow the module pattern:
   ```python
   class MyModule:
       def __init__(self, logger, api_keys=None):
           self.logger = logger
           self.api_keys = api_keys or {}
       
       def run(self, target_ip: str, ports=None) -> Dict[str, Any]:
           # Your implementation
           return {"result": data}
   ```
3. Add to `MODULES` dict in `argus.py`
4. Include docstrings and error handling

### Creating Plugins

1. Create `.py` file in `plugins/` directory
2. Plugin auto-loads on startup via `PluginLoader`
3. Export a `Plugin` class with `config()` and `run()` methods

## ❓ Troubleshooting

### Import errors (colorama/requests not found)
This is a VS Code warning - packages are in `requirements.txt` and will work after installation:
```bash
pip install -r requirements.txt
```

### Port scan timeout
- Increase timeout in `config.py` if scanning slow networks
- Reduce number of ports or use fewer workers
- Check firewall rules

### No GeoIP results
- Verify internet connectivity
- Check that target IP is valid and reachable
- Review logs with `--verbose` flag

### Permission denied on install.sh
```bash
chmod +x install.sh
./install.sh
```

## 📋 Requirements

- Python 3.11+
- `colorama>=0.4.6` - Terminal colors
- `requests>=2.31.0` - HTTP library

See [requirements.txt](requirements.txt) for complete list.

## 📄 License

Proprietary - Defensive Security Analysis Only

## 📞 Support & Licensing

For issues, questions, or feedback:
1. Check [doc/README.md](doc/README.md) for detailed documentation
2. Review logs in `argus.log` (or custom log file)
3. Run with `--verbose` flag for detailed output
4. Check [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for architecture

**For licensing, access requests, or commercial inquiries:**
📧 **Email:** securityxdrew87.variably659@passmail.net

Please include in your request:
- Your full name and organization
- Specific intended use of the Software
- Duration of requested license
- Number of users/systems
- Any relevant business information

---

**Made with ❤️ for cybersecurity professionals and researchers**
