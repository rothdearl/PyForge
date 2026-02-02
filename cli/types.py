"""
Type aliases used throughout the command-line interface package.
"""

import re
from collections.abc import Callable
from typing import Any

type ErrorReporter = Callable[[str], None]
"""Callback for reporting error messages."""

type Json = dict[str, Any]
"""A JSON object: dictionary with string keys and JSON-compatible values."""

type Patterns = list[re.Pattern[str]]
"""List of compiled regular expression patterns."""

__all__ = [
    "ErrorReporter",
    "Json",
    "Patterns"
]
