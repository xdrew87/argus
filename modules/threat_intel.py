"""
ARGUS Threat Intelligence Module
Fetches threat intelligence using secure API handling.
"""
import requests
from typing import Dict, Any

class ThreatIntel:
    """
    ThreatIntel fetches threat intelligence for a target IP.
    """
    def __init__(self, logger, api_keys=None):
        self.logger = logger
        self.api_keys = api_keys or {}

    def run(self, target_ip: str, ports=None) -> Dict[str, Any]:
        """
        Fetches threat intelligence.
        Args:
            target_ip (str): Target IP address.
            ports (str): Unused.
        Returns:
            dict: Threat intelligence results.
        """
        self.logger.info(f"Threat intel started for {target_ip}")
        api_key = self.api_keys.get("threat_intel")
        if not api_key:
            self.logger.warning("No threat intel API key provided.")
            return {"target": target_ip, "threat_intel": "API key missing"}
        try:
            url = f"https://api.threatintel.com/v1/ip/{target_ip}"
            headers = {"Authorization": f"Bearer {api_key}"}
            resp = requests.get(url, headers=headers, timeout=5)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            self.logger.error(f"Threat intel API error: {type(e).__name__}: {e}")
            return {"target": target_ip, "threat_intel": "API error"}
        return {"target": target_ip, "threat_intel": data}
