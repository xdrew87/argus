# ARGUS Project Structure

```
CLI/
├── argus.py                    # Main entry point
├── config.py                   # Configuration & constants
├── demo.py                     # Demo script (no deps)
├── requirements.txt            # Python dependencies
├── install.bat                 # Windows installer
├── install.sh                  # Linux/macOS installer
├── .gitignore                  # Git ignore patterns
│
├── core/                       # Core framework modules
│   ├── __init__.py
│   ├── ui.py                   # Terminal UI & boxed formatting
│   ├── logging.py              # Logging system (file + console)
│   ├── utils.py                # Input validation & helpers
│   └── plugin_loader.py        # Plugin auto-loader
│
├── modules/                    # Security & scanning modules
│   ├── __init__.py
│   ├── network_scanner.py      # Network reachability checks
│   ├── port_scanner.py         # Threaded port scanning
│   ├── breach_checker.py       # Breach database integration
│   ├── ssl_monitor.py          # SSL/TLS certificate checks
│   ├── geoip_lookup.py         # GeoIP geolocation lookup
│   ├── threat_intel.py         # Threat intelligence
│   └── audit_report.py         # Audit report generation
│
├── plugins/                    # External plugins (auto-loaded)
│   └── __init__.py
│
└── doc/                        # Documentation
    ├── README.md               # Full documentation & usage guide
    ├── START_HERE.py           # Quick start guide (executable)
    └── SETUP_COMPLETE.py       # Implementation status report
```

## Clean Root Structure

All documentation has been moved to the `doc/` folder to keep the root clean:
- `doc/README.md` - Full documentation
- `doc/START_HERE.py` - Interactive quick start
- `doc/SETUP_COMPLETE.py` - Implementation summary

## Core Modules (`core/`)

- **ui.py** - ANSI terminal UI with boxed formatting, colors, and headers
- **logging.py** - Dual console/file logging with configurable levels
- **utils.py** - Input validation (IP, hostname, port)
- **plugin_loader.py** - Auto-discovers and loads plugins from `plugins/` directory

## Security Modules (`modules/`)

All modules follow the same pattern:
- `__init__(logger, api_keys)` - Initialize with logger and API keys
- `run(target_ip, ports)` - Execute and return dict results

Modules:
1. **network_scanner.py** - Ping/reachability checks
2. **port_scanner.py** - Threaded port scanning (10 workers)
3. **breach_checker.py** - Breach database lookup
4. **ssl_monitor.py** - SSL certificate validation
5. **geoip_lookup.py** - GeoIP geolocation (free API)
6. **threat_intel.py** - Threat intelligence data
7. **audit_report.py** - Report generation

## Quick Start

```bash
# Install dependencies
install.bat  # Windows
./install.sh # Linux/macOS

# Run tests
python demo.py

# Use ARGUS
python argus.py --help
python argus.py network-scan --target 8.8.8.8
```

For more info, read `doc/README.md` or run `python doc/START_HERE.py`
