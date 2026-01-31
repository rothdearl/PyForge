import unittest
from typing import final

from cli import terminal


@final
class TerminalTest(unittest.TestCase):
    """
    Tests the terminal module.
    """

    def test_terminal_predicates(self) -> None:
        self.assertFalse(terminal.input_is_redirected())
        self.assertTrue(terminal.input_is_terminal())
        self.assertTrue(terminal.output_is_terminal())
