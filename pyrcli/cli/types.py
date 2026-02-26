"""Type aliases used throughout the command-line interface package."""

import re
from collections.abc import Callable
from typing import Any, Final

#: List of compiled regular expression patterns.
type CompiledPatterns = list[re.Pattern[str]]

#: Callback for reporting error messages.
type ErrorReporter = Callable[[str], None]

#: A decoded JSON object represented as a dictionary.
type JsonObject = dict[str, Any]

__all__: Final[tuple[str, ...]] = (
    "CompiledPatterns",
    "ErrorReporter",
    "JsonObject",
)
