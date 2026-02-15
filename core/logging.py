"""
ARGUS Logging System
Provides logging with file output and structured formatting.
"""
import logging
import os
from datetime import datetime

class ArgusLogger:
    """
    ArgusLogger sets up logging to file and console with structured formatting.
    """
    def __init__(self, log_file: str = "argus.log"):
        """
        Initializes the logger.
        Args:
            log_file (str): Path to log file.
        """
        self.log_file = log_file
        self.logger = logging.getLogger("ARGUS")
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        # File handler
        fh = logging.FileHandler(self.log_file)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        # Add handlers
        self.logger.handlers = []
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def info(self, message: str):
        """
        Logs an info message.
        Args:
            message (str): Info message.
        """
        self.logger.info(message)

    def warning(self, message: str):
        """
        Logs a warning message.
        Args:
            message (str): Warning message.
        """
        self.logger.warning(message)

    def error(self, message: str):
        """
        Logs an error message.
        Args:
            message (str): Error message.
        """
        self.logger.error(message)

    def success(self, message: str):
        """
        Logs a success message (INFO level).
        Args:
            message (str): Success message.
        """
        self.logger.info(f"SUCCESS: {message}")
    
    def set_level(self, level: int):
        """
        Sets logging level for logger and handlers.
        Args:
            level (int): logging level (e.g., logging.DEBUG).
        """
        self.logger.setLevel(level)
        for handler in self.logger.handlers:
            handler.setLevel(level)
            handler.setLevel(level)
