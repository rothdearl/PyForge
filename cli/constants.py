"""
Constants used throughout the command-line interface package.
"""

import os
from typing import Final

# OS-related constants.
OS_IS_POSIX: Final[bool] = os.name == "posix"
OS_IS_WINDOWS: Final[bool] = os.name == "nt"

__all__ = ["OS_IS_POSIX", "OS_IS_WINDOWS"]
