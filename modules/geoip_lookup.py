"""
ARGUS GeoIP Lookup Module
Performs GeoIP lookup using secure API handling.
"""
import requests
from typing import Dict, Any

class GeoIPLookup:
    """
    GeoIPLookup performs GeoIP lookup using external APIs.
    """
    def __init__(self, logger, api_keys=None):
        self.logger = logger
        self.api_keys = api_keys or {}

    def run(self, target_ip: str, ports=None) -> Dict[str, Any]:
        """
        Performs GeoIP lookup using suicixde.com API.
        Args:
            target_ip (str): Target IP address.
            ports (str): Unused.
        Returns:
            dict: GeoIP results.
        """
        self.logger.info(f"GeoIP lookup started for {target_ip}")
        try:
            url = f"https://suicixde.com/api/geoip.php?ip={target_ip}"
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            self.logger.error(f"GeoIP API error: {type(e).__name__}: {e}")
            return {"target": target_ip, "geoip": "API error"}
        return {"target": target_ip, "geoip": data}
