"""
Constants for ANSI escape sequences used for terminal text attributes and color output.
"""

from typing import Final as _Final

# Escape with the Control Sequence Introducer.
_CSI: _Final[str] = "\x1b["

# Controls.
RESET: _Final[str] = f"{_CSI}0m"
REVERSE: _Final[str] = f"{_CSI}7m"

# Text attributes.
BLINK: _Final[str] = f"{_CSI}5m"
BOLD: _Final[str] = f"{_CSI}1m"
DIM: _Final[str] = f"{_CSI}2m"
INVISIBLE: _Final[str] = f"{_CSI}8m"
ITALICS: _Final[str] = f"{_CSI}3m"
STRIKETHROUGH: _Final[str] = f"{_CSI}9m"
UNDERLINE: _Final[str] = f"{_CSI}4m"

# Foreground colors.
BLACK: _Final[str] = f"{_CSI}30m"
BLUE: _Final[str] = f"{_CSI}34m"
BRIGHT_BLACK: _Final[str] = f"{_CSI}90m"
BRIGHT_BLUE: _Final[str] = f"{_CSI}94m"
BRIGHT_CYAN: _Final[str] = f"{_CSI}96m"
BRIGHT_GREEN: _Final[str] = f"{_CSI}92m"
BRIGHT_MAGENTA: _Final[str] = f"{_CSI}95m"
BRIGHT_RED: _Final[str] = f"{_CSI}91m"
BRIGHT_WHITE: _Final[str] = f"{_CSI}97m"
BRIGHT_YELLOW: _Final[str] = f"{_CSI}93m"
CYAN: _Final[str] = f"{_CSI}36m"
GREEN: _Final[str] = f"{_CSI}32m"
MAGENTA: _Final[str] = f"{_CSI}35m"
RED: _Final[str] = f"{_CSI}31m"
WHITE: _Final[str] = f"{_CSI}37m"
YELLOW: _Final[str] = f"{_CSI}33m"

# Background colors.
BG_BLACK: _Final[str] = f"{_CSI}40m"
BG_BLUE: _Final[str] = f"{_CSI}44m"
BG_BRIGHT_BLACK: _Final[str] = f"{_CSI}100m"
BG_BRIGHT_BLUE: _Final[str] = f"{_CSI}104m"
BG_BRIGHT_CYAN: _Final[str] = f"{_CSI}106m"
BG_BRIGHT_GREEN: _Final[str] = f"{_CSI}102m"
BG_BRIGHT_MAGENTA: _Final[str] = f"{_CSI}105m"
BG_BRIGHT_RED: _Final[str] = f"{_CSI}101m"
BG_BRIGHT_WHITE: _Final[str] = f"{_CSI}107m"
BG_BRIGHT_YELLOW: _Final[str] = f"{_CSI}103m"
BG_CYAN: _Final[str] = f"{_CSI}46m"
BG_GREEN: _Final[str] = f"{_CSI}42m"
BG_MAGENTA: _Final[str] = f"{_CSI}45m"
BG_RED: _Final[str] = f"{_CSI}41m"
BG_WHITE: _Final[str] = f"{_CSI}47m"
BG_YELLOW: _Final[str] = f"{_CSI}43m"

# ANSI 256-color palette (xterm-compatible).
BG_COLORS_256: _Final[list[str]] = [f"{_CSI}48;5;{i}m" for i in range(256)]
COLORS_256: _Final[list[str]] = [f"{_CSI}38;5;{i}m" for i in range(256)]
