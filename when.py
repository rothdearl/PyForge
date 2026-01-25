#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: when.py
Author: Roth Earl
Version: 0.0.0
Description: A program to display the current calendar, with optional date and time
License: GNU GPLv3
"""

import argparse
import calendar
import datetime
from typing import Final, NamedTuple, final

from cli import CLIProgram, colors


class CalendarQuarterIndex(NamedTuple):
    """
    Immutable container for information about a calendar quarter index.

    :ivar int start: Start of the quarter index.
    :ivar int end: End of the quarter index.
    """
    start: int
    end: int


def color_day_in_week(week: str, day: str, quarter: CalendarQuarterIndex) -> str:
    """
    Colors the day in the week for a calendar quarter.

    :param week: Current week.
    :param day: Current day.
    :param quarter: Current quarter.
    :return: The week with the current day colored.
    """
    colored_text = week[quarter.start:quarter.end].replace(day, reverse_color(day))

    return week[:quarter.start] + colored_text + week[quarter.end:]


def get_calendar_quarter(date: datetime.date) -> CalendarQuarterIndex:
    """
    Returns a CalendarQuarterIndex for the given date.

    :param date: Current date.
    :return: An immutable container for information about a calendar quarter index.
    """
    ranges = {
        0: CalendarQuarterIndex(52, 72),
        1: CalendarQuarterIndex(0, 20),
        2: CalendarQuarterIndex(26, 46)
    }

    return ranges[date.month % 3]


def print_month(date: datetime.date) -> None:
    """
    Prints the current month.

    :param date: Current date.
    """
    month = calendar.month(date.year, date.month, w=0, l=0).splitlines()

    # Print the year header and the days of the week.
    print(month[0])
    print(month[1])

    # Print the weeks highlighting the current day of the month.
    day = f"{date.day:>2}"
    found_day = False

    for output in month[2:]:
        if not found_day and day in output:
            output = output.replace(day, reverse_color(day))
            found_day = True

        print(output)


def print_quarter(date: datetime.date) -> None:
    """
    Prints all the months in the current quarter.

    :param date: Current date.
    """
    month_name = calendar.month_name[date.month]
    quarter = get_calendar_quarter(date)
    year = calendar.calendar(date.year, w=2, l=1, c=6, m=3).splitlines()  # Deliberately use defaults for consistency.

    # Print the year header.
    print(year[0])
    print()

    # Find the current quarter.
    quarter_start = 2

    for output in year[quarter_start:]:
        if month_name in output:
            break

        quarter_start += 1

    # Highlight the current month name.
    year[quarter_start] = year[quarter_start].replace(month_name, reverse_color(month_name))

    # Print the month names and weekdays.
    print(year[quarter_start])
    print(year[quarter_start + 1])

    # Print the weeks highlighting the current day of the current month.
    day = f"{date.day:>2}"
    found_day = False

    for output in year[quarter_start + 2:]:
        if not output:  # End of quarter?
            break

        if not found_day and day in output[quarter.start:quarter.end]:
            output = color_day_in_week(output, day, quarter)
            found_day = True

        print(output)


def print_year(date: datetime.date) -> None:
    """
    Prints all the months in the current year.

    :param date: Current date.
    """
    month_name = calendar.month_name[date.month]
    quarter = get_calendar_quarter(date)
    year = calendar.calendar(date.year, w=2, l=1, c=6, m=3).splitlines()  # Deliberately use defaults for consistency.

    # Print the months highlighting the current month and the current day.
    day = f"{date.day:>2}"
    found_day, found_month = False, False

    for output in year:
        if not found_month and month_name in output:
            output = output.replace(month_name, reverse_color(month_name))
            found_month = True

        if not found_day and found_month and day in output[quarter.start:quarter.end]:
            output = color_day_in_week(output, day, quarter)
            found_day = True

        print(output)


def reverse_color(value: str) -> str:
    """
    Reverses the color for the value.

    :param value: Value to reverse color for.
    :return: The value with reversed color.
    """
    return f"{colors.REVERSE}{value}{colors.RESET}"


@final
class When(CLIProgram):
    """
    A program to display the current calendar, with optional date and time

    :cvar Final[str] DEFAULT_DATETIME_FORMAT: Default format for printing the date and time.
    """

    DEFAULT_DATETIME_FORMAT: Final[str] = "%a %b %-d %-I:%M%p"

    def __init__(self) -> None:
        """
        Initializes a new instance.
        """
        super().__init__(name="when", version="0.0.0")

    def build_arguments(self) -> argparse.ArgumentParser:
        """
        Builds and returns an argument parser.

        :return: An argument parser.
        """
        parser = argparse.ArgumentParser(allow_abbrev=False,
                                         description="display the current calendar, with optional date and time",
                                         epilog=f"datetime format is interpreted using strftime(3)", prog=self.NAME)
        parser.add_argument("-c", "--calendar", choices=("m", "q", "y"), default="m",
                            help="print calendar as a month, quarter, or year (default: m)")
        parser.add_argument("-d", "--datetime", action="store_true",
                            help="print current date and time after calendar output")
        parser.add_argument("-w", "--week-start", choices=("mon", "sun"), default="mon",
                            help="set first day of week to monday or sunday (default: mon)")
        parser.add_argument("--datetime-format", help="use STRING as the datetime format", metavar="STRING")
        parser.add_argument("--version", action="version", version=f"%(prog)s {self.VERSION}")

        return parser

    def main(self) -> None:
        """
        The main function of the program.
        """
        today = datetime.date.today()

        if self.args.week_start == "sun":  # --week-start
            calendar.setfirstweekday(calendar.SUNDAY)

        match self.args.calendar:  # --calendar
            case "m":
                print_month(today)
            case "q":
                print_quarter(today)
            case _:
                print_year(today)

        if self.args.datetime:  # --datetime
            date_format = self.args.datetime_format or When.DEFAULT_DATETIME_FORMAT  # --datetime-format

            print()
            print(datetime.datetime.now().strftime(date_format))

    def validate_parsed_arguments(self) -> None:
        """
        Validates the parsed command-line arguments.
        :return: None
        """
        pass


if __name__ == "__main__":
    When().run()
