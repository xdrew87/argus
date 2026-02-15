"""
ARGUS SSL Monitor Module
Checks SSL certificate status for target.
"""
import ssl
import socket
from typing import Dict, Any

class SSLMonitor:
    """
    SSLMonitor checks SSL certificate status for a target.
    """
    def __init__(self, logger, api_keys=None):
        self.logger = logger
        self.api_keys = api_keys or {}

    def run(self, target_ip: str, ports=None) -> Dict[str, Any]:
        """
        Checks SSL certificate status.
        Args:
            target_ip (str): Target IP address.
            ports (str): Optional port (default 443).
        Returns:
            dict: SSL status.
        """
        port = 443
        if ports:
            try:
                port = int(ports.split(",")[0])
            except Exception:
                port = 443
        self.logger.info(f"SSL monitor started for {target_ip}:{port}")
        try:
            context = ssl.create_default_context()
            with socket.create_connection((target_ip, port), timeout=3) as sock:
                with context.wrap_socket(sock, server_hostname=target_ip) as ssock:
                    cert = ssock.getpeercert()
            status = "valid" if cert else "invalid"
        except Exception as e:
            self.logger.error(f"SSL check error: {type(e).__name__}: {e}")
            status = "error"
            cert = None
        return {"target": target_ip, "port": port, "ssl_status": status, "certificate": cert}
