"""
ABC base class for command-line programs.
"""

import argparse
import os
import sys
from abc import ABC, abstractmethod
from typing import Final, final

from cli import terminal


class CLIProgram(ABC):
    """
    ABC base class for command-line programs.

    :ivar int ERROR_EXIT_CODE: Exit code when an error occurs (default: 1).
    :ivar str NAME: Program name.
    :ivar str VERSION: Program version.
    :ivar argparse.Namespace args: Parsed command-line arguments.
    :ivar str encoding: Encoding for reading and writing to files.
    :ivar bool has_errors: Whether the program has encountered errors.
    :ivar bool print_color: Whether color output is enabled.
    """

    def __init__(self, *, name: str, version: str, error_exit_code: int = 1) -> None:
        """
        Initializes a new instance.

        :param name: Program name.
        :param version: Program version.
        :param error_exit_code: Exit code when an error occurs (default: 1).
        """
        self.ERROR_EXIT_CODE: Final[int] = error_exit_code
        self.NAME: Final[str] = name
        self.VERSION: Final[str] = version
        self.args: argparse.Namespace | None = None
        self.encoding: str | None = None
        self.has_errors: bool = False
        self.print_color: bool = False

    @abstractmethod
    def build_arguments(self) -> argparse.ArgumentParser:
        """
        Builds an argument parser.

        :return: An argument parser.
        """
        ...

    def check_for_errors(self) -> None:
        """
        Raises a SystemExit if there are any errors.

        :raises SystemExit: Request to exit from the interpreter if there are any errors.
        """
        if self.has_errors:
            raise SystemExit(self.ERROR_EXIT_CODE)

    @abstractmethod
    def main(self) -> None:
        """
        The main function of the program.
        """
        ...

    @final
    def parse_arguments(self) -> None:
        """
        Parses the command line arguments to get the program options.
        """
        self.args = self.build_arguments().parse_args()
        self.encoding = "iso-8859-1" if getattr(self.args, "latin1", False) else "utf-8"  # --latin1
        self.print_color = getattr(self.args, "color", "off") == "on" and terminal.output_is_terminal()  # --color

    @final
    def print_error(self, error_message: str) -> None:
        """
        Sets the error flag to True and prints the error message to standard error if the argument no_messages = False.

        :param error_message: Error message to print.
        """
        self.has_errors = True

        if not getattr(self.args, "no_messages", False):
            print(f"{self.NAME}: error: {error_message}", file=sys.stderr)

    @final
    def print_error_and_exit(self, error_message: str) -> None:
        """
        Prints the error message to standard error and raises a SystemExit.

        :param error_message: Error message to print.
        """
        print(f"{self.NAME}: error: {error_message}", file=sys.stderr)
        raise SystemExit(self.ERROR_EXIT_CODE)

    @final
    def run(self) -> None:
        """
        Runs the program.
        """
        keyboard_interrupt_error_code = 130
        windows = os.name == "nt"

        try:
            if windows:  # Fix ANSI escape sequences on Windows.
                from colorama import just_fix_windows_console

                just_fix_windows_console()
            else:  # Prevent broken pipe errors (not supported on Windows).
                from signal import SIG_DFL, SIGPIPE, signal

                signal(SIGPIPE, SIG_DFL)

            self.parse_arguments()
            self.validate_parsed_arguments()
            self.main()
            self.check_for_errors()
        except KeyboardInterrupt:
            print()  # Add a newline after Ctrl-C.
            raise SystemExit(self.ERROR_EXIT_CODE if windows else keyboard_interrupt_error_code)
        except OSError as e:
            raise SystemExit(self.ERROR_EXIT_CODE) from e

    @abstractmethod
    def validate_parsed_arguments(self) -> None:
        """
        Validates the parsed command-line arguments.
        """
        ...
