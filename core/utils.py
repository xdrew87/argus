"""
ARGUS Utilities
Provides input validation, hostname resolution, and secure helpers.
"""
import ipaddress
import socket
from typing import Union

class ArgusUtils:
    """
    ArgusUtils provides static methods for input validation and resolution.
    """
    @staticmethod
    def validate_ip(ip: str) -> bool:
        """
        Validates an IPv4 or IPv6 address.
        Args:
            ip (str): IP address.
        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def resolve_hostname(hostname: str) -> Union[str, None]:
        """
        Resolves a hostname to an IP address.
        Args:
            hostname (str): Hostname to resolve.
        Returns:
            str or None: IP address or None if resolution fails.
        """
        try:
            return socket.gethostbyname(hostname)
        except (socket.gaierror, UnicodeError):
            return None

    @staticmethod
    def validate_port(port: Union[str, int]) -> bool:
        """
        Validates a port number.
        Args:
            port (str|int): Port number.
        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            port = int(port)
            return 0 < port < 65536
        except (ValueError, TypeError):
            return False
