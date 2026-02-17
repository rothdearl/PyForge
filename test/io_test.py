import unittest
from typing import final

from cli import io


@final
class IOTest(unittest.TestCase):
    """Tests the ios module."""

    def test_normalize_input_lines(self) -> None:
        """Tests the normalize_input_lines function."""
        lines = (
            "Line 1\n",
            "Line 2",
            "Line 3\n",
            "Line 4",
            "Line 5\n"
        )

        for line in io.normalize_input_lines(lines):
            self.assertFalse(line.endswith("\n"))

    def test_read_text_files(self) -> None:
        """Tests the read_text_files function."""
        errors = []

        def on_error(error_message: str) -> None:
            """Callback for on_error."""
            errors.append(error_message)

        # 1) Empty file list.
        io.read_text_files(files=[], encoding="utf-8", on_error=on_error)
        self.assertEqual(errors, [])

        # 2) Valid file.
        for file_info in io.read_text_files(files=["__init__.py"], encoding="utf-8", on_error=on_error):
            self.assertEqual(file_info.file_name, "__init__.py")
        self.assertEqual(errors, [])

        # 3) File error: no such file or directory.
        for _ in io.read_text_files(files=["_init_.py"], encoding="utf-8", on_error=on_error):
            pass
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "_init_.py: no such file or directory")
        errors.clear()

        # 4) File error: is a directory.
        for _ in io.read_text_files(files=["__pycache__"], encoding="utf-8", on_error=on_error):
            pass
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "__pycache__: is a directory")

    def test_remove_trailing_newline(self) -> None:
        """Tests the remove_trailing_newline function."""
        lines = (
            "Line 1\n",
            "Line 2",
            "Line 3\n",
            "Line 4",
            "Line 5\n"
        )

        for line in lines:
            self.assertFalse(io.remove_trailing_newline(line).endswith("\n"))

    def test_write_text_to_file(self) -> None:
        """Tests the write_text_to_file function."""
        errors = []

        def on_error(error_message: str) -> None:
            """Callback for on_error."""
            errors.append(error_message)

        # 1) Valid file.
        io.write_text_to_file("io-test-file.txt", text=["Unit testing."], encoding="utf-8", on_error=on_error)
        self.assertEqual(errors, [])

        # 2) Empty file name.
        io.write_text_to_file("", text=[], encoding="utf-8", on_error=on_error)
        self.assertEqual(len(errors), 1)
        errors.clear()

        # 3) Valid encoding.
        io.write_text_to_file("io-test-file.txt", text=["Unit testing."], encoding="invalid", on_error=on_error)
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], "io-test-file.txt: unknown encoding invalid")
