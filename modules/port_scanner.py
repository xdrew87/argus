"""
ARGUS Port Scanner Module
Threaded port scanning using ThreadPoolExecutor.
"""
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, List

class PortScanner:
    """
    PortScanner performs threaded port scanning.
    """
    def __init__(self, logger, api_keys=None):
        self.logger = logger
        self.api_keys = api_keys or {}

    def scan_port(self, target_ip: str, port: int) -> Dict[str, Any]:
        """
        Scans a single port.
        Args:
            target_ip (str): Target IP address.
            port (int): Port number.
        Returns:
            dict: Port scan result.
        """
        result = {"port": port, "open": False}
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                if sock.connect_ex((target_ip, port)) == 0:
                    result["open"] = True
        except Exception as e:
            self.logger.warning(f"Port {port} scan error: {type(e).__name__}: {e}")
        return result

    def run(self, target_ip: str, ports=None) -> Dict[str, Any]:
        """
        Runs threaded port scan.
        Args:
            target_ip (str): Target IP address.
            ports (str): Comma-separated ports.
        Returns:
            dict: Scan results.
        """
        self.logger.info(f"Port scan started for {target_ip}")
        port_list: List[int] = []
        if ports:
            port_list = [int(p.strip()) for p in ports.split(",") if p.strip().isdigit()]
        else:
            port_list = [22, 80, 443, 8080]  # Default ports
        results = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.scan_port, target_ip, port) for port in port_list]
            for future in as_completed(futures):
                results.append(future.result())
        self.logger.info(f"Port scan results: {results}")
        return {"target": target_ip, "ports": results}
