import unittest
from typing import final

from cli import ansi


@final
class ANSITest(unittest.TestCase):
    """
    Tests the ansi module.
    """

    def test_256_color_palette(self) -> None:
        # Verify lengths.
        self.assertEqual(len(ansi.BG_COLORS_256), 256)
        self.assertEqual(len(ansi.COLORS_256), 256)

        # Print the ANSI text attributes.
        print(f"ANSI text attributes")

        for attribute in ansi.TextAttributes:
            print(f"[{attribute.name:<13}]: {attribute}The quick brown fox jumps over the lazy dog{ansi.RESET}")

        print()

        # Print the forground colors.
        print(f"ANSI 16-color palette foreground colors")

        for fg_color in ansi.Colors16:
            print(f"[{fg_color.name:<14}]: {fg_color}The quick brown fox jumps over the lazy dog{ansi.RESET}")

        print()

        # Print the background colors.
        print(f"ANSI 16-color palette background colors")

        for bg_color in ansi.BGColors16:
            print(f"[{bg_color.name:<17}]: {bg_color}The quick brown fox jumps over the lazy dog{ansi.RESET}")

        print()

        # Print the ANSI 256-colors.
        print("ANSI 256-color palette (xterm-compatible)")

        for index, (fg_color, bg_color) in enumerate(zip(ansi.COLORS_256, ansi.BG_COLORS_256)):
            print(
                f"[{index:>3}]: {fg_color}The quick brown fox jumps{ansi.RESET} {bg_color}over the lazy dog{ansi.RESET}")
