"""
ARGUS Quick Start Guide and README
"""

# ARGUS - Advanced Security Intelligence Platform

A modular, production-quality cybersecurity CLI framework for security analysis, monitoring, and reporting.

## Features

- **Modular Architecture**: Core components (UI, logging, utilities) + reusable security modules
- **Threaded Port Scanning**: Fast concurrent port scanning using ThreadPoolExecutor
- **Multiple Security Modules**:
  - Network Scanner: Basic network visibility and reachability checks
  - Port Scanner: Threaded multi-port scanning
  - Breach Checker: Integration with breach intelligence APIs
  - SSL Monitor: Certificate status and validity checks
  - GeoIP Lookup: Geographic and network information
  - Threat Intelligence: Threat data enrichment
  - Audit Report: Comprehensive security reports
  
- **Plugin System**: Auto-load external modules from plugins/ directory
- **JSON Export**: Export all results as JSON reports
- **Comprehensive Logging**: File and console logging with multiple levels
- **Secure API Handling**: Environment variable-based API key management
- **Cross-Platform**: Windows, Linux, macOS compatible
- **Production-Ready**: Error handling, input validation, secure coding practices

## Installation

### Windows
```bash
install.bat
```

### Linux/macOS
```bash
chmod +x install.sh
./install.sh
```

### Manual
```bash
pip install -r requirements.txt
```

## Usage

### Display Help
```bash
python argus.py --help
```

### Network Scanning
```bash
python argus.py network-scan --target 8.8.8.8
```

### Port Scanning
```bash
python argus.py port-scan --target 8.8.8.8 --ports 80,443,8080
```

### GeoIP Lookup
```bash
python argus.py geoip --target 8.8.8.8 --output geoip_report.json
```

### With Verbose Logging
```bash
python argus.py network-scan --target 8.8.8.8 --verbose
```

### Export to JSON Report
```bash
python argus.py port-scan --target 192.168.1.1 --ports 22,80,443 --output scan_report.json
```

## Environment Variables

For secure API key management, set environment variables:

```bash
# Windows
set ARGUS_LOG_FILE=custom.log
set ARGUS_GEOIP_API_KEY=your_key_here
set ARGUS_THREAT_INTEL_API_KEY=your_key_here

# Linux/macOS
export ARGUS_LOG_FILE=custom.log
export ARGUS_GEOIP_API_KEY=your_key_here
export ARGUS_THREAT_INTEL_API_KEY=your_key_here
```

## Project Structure

```
CLI/
├── argus.py              # Main entry point
├── config.py             # Configuration and constants
├── requirements.txt      # Python dependencies
├── install.bat           # Windows installer
├── install.sh            # Linux/macOS installer
├── core/
│   ├── __init__.py
│   ├── ui.py             # Terminal UI and formatting
│   ├── logging.py        # Logging system
│   ├── utils.py          # Input validation and utilities
│   └── plugin_loader.py  # Plugin auto-loader
├── modules/
│   ├── __init__.py
│   ├── network_scanner.py    # Network visibility checks
│   ├── port_scanner.py       # Threaded port scanning
│   ├── breach_checker.py     # Breach intelligence
│   ├── ssl_monitor.py        # SSL certificate checks
│   ├── geoip_lookup.py       # GeoIP lookups
│   ├── threat_intel.py       # Threat intelligence
│   └── audit_report.py       # Report generation
└── plugins/              # External plugins (auto-loaded)
```

## Design Philosophy

ARGUS is a **defensive and analytical platform** focused on:
- **Visibility**: Understanding the security landscape
- **Monitoring**: Continuous observation of security posture
- **Reporting**: Actionable security intelligence
- **Compliance**: Audit trails and structured reporting

NOT for exploitation or unauthorized access.

## Development Standards

- Python 3.11+
- PEP 8 compliant
- Secure coding practices (no bare except, proper error handling)
- Full docstrings on all classes and functions
- Environment-based secret management
- Cross-platform compatibility
- Production-quality error handling

## Security Notes

- **Never hardcode API keys** - use environment variables
- **Validate all inputs** - IP addresses, ports, hostnames use built-in validators
- **Handle errors gracefully** - no sensitive information leakage
- **Use HTTPS** - all API calls should use secure endpoints
- **Log responsibly** - sensitive data should be redacted in logs

## Troubleshooting

### "Import colorama/requests not resolved"
This is a VS Code warning - packages are in requirements.txt and will work after installation.

### Port scan times out
- Increase timeout in config.py if scanning slow networks
- Reduce number of ports or use fewer workers

### No results from GeoIP
- Verify ARGUS_GEOIP_API_KEY environment variable is not set (public API key is embedded)
- Check internet connectivity
- Verify target IP is valid

## Contributing

To add new modules:

1. Create new file in `modules/`
2. Inherit from base pattern (init with logger/api_keys, run method returns dict)
3. Add to MODULES dict in argus.py
4. Follow PEP 8 and include docstrings

To create plugins:

1. Create .py file in `plugins/`
2. Plugin auto-loads on startup via PluginLoader
3. Make sure plugin exports a `Plugin` class with config/run methods

## License

Proprietary - Defensive Security Analysis Only

## Support

For issues or questions, review logs in argus.log or enable --verbose mode for detailed output.
