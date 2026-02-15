"""
ARGUS Plugin Loader
Auto-loads external modules from plugins/ securely.
"""
import importlib.util
import os
from types import ModuleType
from typing import List

class PluginLoader:
    """
    PluginLoader loads Python modules from the plugins directory securely.
    """
    def __init__(self, plugins_dir: str = "plugins"):
        """
        Initializes the plugin loader.
        Args:
            plugins_dir (str): Directory containing plugins.
        """
        self.plugins_dir = plugins_dir
        self.plugins: List[ModuleType] = []

    def load_plugins(self) -> List[ModuleType]:
        """
        Loads all valid Python plugin modules from the plugins directory.
        Returns:
            List[ModuleType]: List of loaded plugin modules.
        """
        self.plugins = []
        if not os.path.isdir(self.plugins_dir):
            return self.plugins
        for fname in os.listdir(self.plugins_dir):
            if fname.endswith(".py") and not fname.startswith("_"):
                path = os.path.join(self.plugins_dir, fname)
                try:
                    spec = importlib.util.spec_from_file_location(fname[:-3], path)
                    if spec and spec.loader:
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)
                        self.plugins.append(module)
                except Exception as e:
                    # Log securely, do not expose sensitive info
                    print(f"[PluginLoader] Failed to load {fname}: {type(e).__name__}")
        return self.plugins
