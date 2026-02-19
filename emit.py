#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A program that writes strings to standard output."""

import argparse
import sys
from collections.abc import Iterable
from typing import override

from cli import CLIProgram, terminal, text


class Emit(CLIProgram):
    """A program that writes strings to standard output."""

    def __init__(self) -> None:
        """Initialize a new ``Emit`` instance."""
        super().__init__(name="emit", version="1.0.0")

    @override
    def build_arguments(self) -> argparse.ArgumentParser:
        """Build and return an argument parser."""
        parser = argparse.ArgumentParser(allow_abbrev=False, description="write strings to standard output",
                                         prog=self.name)

        parser.add_argument("strings", help="strings to write", metavar="STRINGS", nargs="*")
        parser.add_argument("-n", "--no-newline", action="store_true", help="suppress trailing newline")
        parser.add_argument("-e", "--escape-sequences", action="store_true",
                            help="interpret backslash escapes (disabled by default)")
        parser.add_argument("--version", action="version", version=f"%(prog)s {self.version}")

        return parser

    @override
    def main(self) -> None:
        """Run the program."""
        print_newline = not self.args.no_newline

        self.write_strings(self.args.strings)

        if terminal.stdin_is_redirected():
            self.write_strings(sys.stdin)

        print(end="\n" if print_newline else "")

    def write_strings(self, strings: Iterable[str]) -> None:
        """Write strings to standard output."""
        print_space = False

        for string in text.iter_normalized_lines(strings):
            if print_space:  # Prefix strings with a space character to avoid a trailing space character.
                print(" ", end="")

            if self.args.escape_sequences:
                try:
                    print(text.decode_python_escape_sequences(string), end="")
                except UnicodeDecodeError:
                    self.print_error_and_exit(f"invalid escape sequence in: {string!r}")
            else:
                print(string, end="")

            print_space = True


if __name__ == "__main__":
    Emit().run()
