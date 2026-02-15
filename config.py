"""
ARGUS Configuration and Constants
"""
import os

# Application Settings
APP_NAME = "ARGUS"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Advanced Security Intelligence Platform"

# Logging
LOG_FILE = os.environ.get("ARGUS_LOG_FILE", "argus.log")
LOG_LEVEL = os.environ.get("ARGUS_LOG_LEVEL", "INFO")

# API Keys (Load from environment for security)
API_KEYS = {
    "geoip": os.environ.get("ARGUS_GEOIP_API_KEY"),
    "threat_intel": os.environ.get("ARGUS_THREAT_INTEL_API_KEY"),
    "breach": os.environ.get("ARGUS_BREACH_API_KEY"),
}

# Default Port Scan Ports
DEFAULT_PORTS = [22, 80, 443, 8080, 3389, 5432, 3306]

# Timeout Settings (seconds)
SOCKET_TIMEOUT = 3
HTTP_TIMEOUT = 5
PORT_SCAN_TIMEOUT = 1

# Threading
MAX_WORKERS = 10

# API Endpoints
GEOIP_API = "https://suicixde.com/api/geoip.php?ip={ip}"
