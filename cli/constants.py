"""
Constants used throughout the command-line interface package.
"""

import os as _os
import sys as _sys
from typing import Final as _Final

# OS-related constants.
OS_IS_LINUX: _Final[bool] = _sys.platform.startswith("linux")
OS_IS_MAC: _Final[bool] = _sys.platform == "darwin"
OS_IS_POSIX: _Final[bool] = _os.name == "posix"
OS_IS_WINDOWS: _Final[bool] = _sys.platform == "win32"

__all__ = [
    "OS_IS_LINUX",
    "OS_IS_MAC",
    "OS_IS_POSIX",
    "OS_IS_WINDOWS"
]
