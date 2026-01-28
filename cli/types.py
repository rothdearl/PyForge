"""
Type aliases used throughout the command-line interface package.
"""

import re
from collections.abc import Callable, Iterable
from typing import Any, TypeAlias

CompiledPatterns: TypeAlias = list[re.Pattern[str]]
ErrorReporter: TypeAlias = Callable[[str], None]
Json: TypeAlias = dict[str, Any]
PatternGroups: TypeAlias = Iterable[re.Pattern[str]]

__all__ = [
    "CompiledPatterns",
    "ErrorReporter",
    "Json",
    "PatternGroups"
]
