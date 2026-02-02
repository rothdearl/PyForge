"""
Define constants for ANSI escape sequences used for terminal text attributes and color output.
"""

from enum import StrEnum
from typing import Final

# Control Sequence Introducer (CSI).
_CSI: Final[str] = "\x1b["

#: Reset all SGR attributes and colors.
RESET: Final[str] = f"{_CSI}0m"


class BGColors16(StrEnum):
    """
    16-color palette background color constants (SGR codes 40–47 and 100–107).
    """
    BG_BLACK = f"{_CSI}40m"
    BG_RED = f"{_CSI}41m"
    BG_GREEN = f"{_CSI}42m"
    BG_YELLOW = f"{_CSI}43m"
    BG_BLUE = f"{_CSI}44m"
    BG_MAGENTA = f"{_CSI}45m"
    BG_CYAN = f"{_CSI}46m"
    BG_WHITE = f"{_CSI}47m"
    BG_BRIGHT_BLACK = f"{_CSI}100m"
    BG_BRIGHT_RED = f"{_CSI}101m"
    BG_BRIGHT_GREEN = f"{_CSI}102m"
    BG_BRIGHT_YELLOW = f"{_CSI}103m"
    BG_BRIGHT_BLUE = f"{_CSI}104m"
    BG_BRIGHT_MAGENTA = f"{_CSI}105m"
    BG_BRIGHT_CYAN = f"{_CSI}106m"
    BG_BRIGHT_WHITE = f"{_CSI}107m"


class Colors16(StrEnum):
    """
    16-color palette foreground color constants (SGR codes 30–37 and 90–97).
    """
    BLACK = f"{_CSI}30m"
    RED = f"{_CSI}31m"
    GREEN = f"{_CSI}32m"
    YELLOW = f"{_CSI}33m"
    BLUE = f"{_CSI}34m"
    MAGENTA = f"{_CSI}35m"
    CYAN = f"{_CSI}36m"
    WHITE = f"{_CSI}37m"
    BRIGHT_BLACK = f"{_CSI}90m"
    BRIGHT_RED = f"{_CSI}91m"
    BRIGHT_GREEN = f"{_CSI}92m"
    BRIGHT_YELLOW = f"{_CSI}93m"
    BRIGHT_BLUE = f"{_CSI}94m"
    BRIGHT_MAGENTA = f"{_CSI}95m"
    BRIGHT_CYAN = f"{_CSI}96m"
    BRIGHT_WHITE = f"{_CSI}97m"


class TextAttributes(StrEnum):
    """
    Text attribute constants (SGR codes 1–9 except 6 which is undefined).
    """
    BOLD = f"{_CSI}1m"
    DIM = f"{_CSI}2m"
    ITALIC = f"{_CSI}3m"
    UNDERLINE = f"{_CSI}4m"
    BLINK = f"{_CSI}5m"
    REVERSE = f"{_CSI}7m"
    INVISIBLE = f"{_CSI}8m"
    STRIKETHROUGH = f"{_CSI}9m"


# 256-color palettes (xterm-compatible SGR codes 38;5;0–255 and 48;5;0–255).
BG_COLORS_256: Final[tuple[str, ...]] = tuple(f"{_CSI}48;5;{code}m" for code in range(256))
COLORS_256: Final[tuple[str, ...]] = tuple(f"{_CSI}38;5;{code}m" for code in range(256))

__all__ = [
    "BGColors16",
    "BG_COLORS_256",
    "COLORS_256",
    "Colors16",
    "RESET",
    "TextAttributes",
]
