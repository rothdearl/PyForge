"""
ANSI escape sequences.
"""

# Escape with the Control Sequence Introducer.
_CSI = "\x1b["

# Controls.
RESET = f"{_CSI}0m"
REVERSE = f"{_CSI}7m"

# Text attributes.
BLINK = f"{_CSI}5m"
BOLD = f"{_CSI}1m"
DIM = f"{_CSI}2m"
INVISIBLE = f"{_CSI}8m"
ITALICS = f"{_CSI}3m"
STRIKETHROUGH = f"{_CSI}9m"
UNDERLINE = f"{_CSI}4m"

# Foreground colors.
BLACK = f"{_CSI}30m"
BLUE = f"{_CSI}34m"
BRIGHT_BLACK = f"{_CSI}90m"
BRIGHT_BLUE = f"{_CSI}94m"
BRIGHT_CYAN = f"{_CSI}96m"
BRIGHT_GREEN = f"{_CSI}92m"
BRIGHT_MAGENTA = f"{_CSI}95m"
BRIGHT_RED = f"{_CSI}91m"
BRIGHT_WHITE = f"{_CSI}97m"
BRIGHT_YELLOW = f"{_CSI}93m"
CYAN = f"{_CSI}36m"
GREEN = f"{_CSI}32m"
MAGENTA = f"{_CSI}35m"
RED = f"{_CSI}31m"
WHITE = f"{_CSI}37m"
YELLOW = f"{_CSI}33m"

# Background colors.
BG_BLACK = f"{_CSI}40m"
BG_BLUE = f"{_CSI}44m"
BG_BRIGHT_BLACK = f"{_CSI}100m"
BG_BRIGHT_BLUE = f"{_CSI}104m"
BG_BRIGHT_CYAN = f"{_CSI}106m"
BG_BRIGHT_GREEN = f"{_CSI}102m"
BG_BRIGHT_MAGENTA = f"{_CSI}105m"
BG_BRIGHT_RED = f"{_CSI}101m"
BG_BRIGHT_WHITE = f"{_CSI}107m"
BG_BRIGHT_YELLOW = f"{_CSI}103m"
BG_CYAN = f"{_CSI}46m"
BG_GREEN = f"{_CSI}42m"
BG_MAGENTA = f"{_CSI}45m"
BG_RED = f"{_CSI}41m"
BG_WHITE = f"{_CSI}47m"
BG_YELLOW = f"{_CSI}43m"
