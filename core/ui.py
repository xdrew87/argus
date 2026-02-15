"""
ARGUS Terminal UI Utilities
Provides ANSI terminal UI with structured boxed formatting.
"""
import sys
import os
import shutil
import platform
import datetime
from typing import List

try:
    from colorama import Fore, Style
except ImportError:
    Fore = Style = type('Dummy', (), {'GREEN': '', 'RESET_ALL': ''})

class TerminalUI:
    """
    TerminalUI provides methods for displaying structured, boxed, and colored output in the terminal.
    """
    ANSI_RESET = '\033[0m'
    ANSI_BOLD = '\033[1m'
    ANSI_BOX = '\033[34m'  # Blue
    ANSI_ERROR = '\033[31m'  # Red
    ANSI_SUCCESS = '\033[32m'  # Green
    ANSI_WARNING = '\033[33m'  # Yellow

    @staticmethod
    def print_header():
        """
        Prints the application header with boxed formatting and dynamic system info.
        """
        term_width = shutil.get_terminal_size((80, 20)).columns
        box_width = min(70, term_width - 2)
        title = "🛡 ARGUS v1.0 🛡"
        subtitle = "Advanced Security Intelligence Platform"
        system_info = f"{platform.system()} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        def center_text(text):
            return text.center(box_width - 2)
        top_border = "╔" + "═" * (box_width - 2) + "╗"
        bottom_border = "╚" + "═" * (box_width - 2) + "╝"
        empty_line = "║" + " " * (box_width - 2) + "║"
        header_lines = [
            top_border,
            empty_line,
            f"║{center_text(title)}║",
            f"║{center_text(subtitle)}║",
            empty_line,
            f"║{center_text(system_info)}║",
            empty_line,
            bottom_border
        ]
        print(Fore.GREEN + "\n".join(header_lines) + Style.RESET_ALL)

    @staticmethod
    def boxed(text: str, color: str = None) -> str:
        """
        Returns a string formatted in a box with ANSI color.
        Args:
            text (str): The text to display.
            color (str): ANSI color code.
        Returns:
            str: Boxed and colored text.
        """
        if color is None:
            color = TerminalUI.ANSI_BOX
        lines = text.split('\n')
        width = max(len(line) for line in lines) if lines else 0
        top = f"{color}+{'-' * (width + 2)}+{TerminalUI.ANSI_RESET}"
        boxed_lines = [top]
        for line in lines:
            boxed_lines.append(f"{color}| {line.ljust(width)} |{TerminalUI.ANSI_RESET}")
        boxed_lines.append(top)
        return '\n'.join(boxed_lines)

    @staticmethod
    def print_boxed(text: str, color: str = None):
        """
        Prints boxed text to terminal.
        Args:
            text (str): The text to display.
            color (str): ANSI color code.
        """
        if color is None:
            color = TerminalUI.ANSI_BOX
        print(TerminalUI.boxed(text, color))

    @staticmethod
    def print_error(message: str):
        """
        Prints an error message in a red box.
        Args:
            message (str): Error message.
        """
        TerminalUI.print_boxed(message, TerminalUI.ANSI_ERROR)

    @staticmethod
    def print_success(message: str):
        """
        Prints a success message in a green box.
        Args:
            message (str): Success message.
        """
        TerminalUI.print_boxed(message, TerminalUI.ANSI_SUCCESS)

    @staticmethod
    def print_warning(message: str):
        """
        Prints a warning message in a yellow box.
        Args:
            message (str): Warning message.
        """
        TerminalUI.print_boxed(message, TerminalUI.ANSI_WARNING)
