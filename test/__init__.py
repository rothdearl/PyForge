"""
Initialization file for the test package.
"""

from .ansi_test import ANSITest
from .ini_test import INITest

from .patterns_test import (
    TestColorPatternMatches,
    TestCompileCombinedPatterns,
    TestCompilePatterns,
    TestMatchesAllPatterns
)

from .terminal_test import TerminalTest
