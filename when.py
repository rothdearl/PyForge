#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Filename: when.py
Author: Roth Earl
Version: 0.0.0
Description: A program to display the current calendar and time.
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

    :ivar start: Start of the quarter index.
    :ivar end: End of the quarter index.
    """
    start: int
    end: int


@final
class When(CLIProgram):
    """
    A program to display the current calendar and time.

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
        parser = argparse.ArgumentParser(allow_abbrev=False, description="display the current calendar and time",
                                         epilog=f"datetime format is interpreted using strftime(3)", prog=self.NAME)
        parser.add_argument("-c", "--calendar", choices=("m", "q", "y"), default="m",
                            help="print calendar as a month, quarter or year (default: m)")
        parser.add_argument("-d", "--datetime", action="store_true",
                            help="print current date and time with calendar output")
        parser.add_argument("-w", "--week-start", choices=("mon", "sun"), default="m",
                            help="set first day of week to monday or sunday (default: mon)")
        parser.add_argument("--datetime-format", help="use STRING for format used in datetime output", metavar="STRING")
        parser.add_argument("--version", action="version", version=f"%(prog)s {self.VERSION}")

        return parser

    @staticmethod
    def color_day_in_week(day: str, week: str, quarter: CalendarQuarterIndex) -> str:
        """
        Colors the day in the week from a calendar quarter.

        :param day: Current day.
        :param week: Current week.
        :param quarter: Current quarter.
        :return: The week with the current day colored.
        """
        colored_text = week[quarter.start:quarter.end].replace(day, When.reverse_color(day))

        return week[:quarter.start] + colored_text + week[quarter.end:]

    @staticmethod
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

    def main(self) -> None:
        """
        The main function of the program.
        """
        today = datetime.date.today()

        if self.args.week_start == "sun":  # --week-start
            calendar.setfirstweekday(calendar.SUNDAY)

        match self.args.calendar:  # --calendar
            case "m":
                When.print_month(today)
            case "q":
                When.print_quarter(today)
            case _:
                When.print_year(today)

        if self.args.datetime:  # --datetime
            date_format = self.args.datetime_format or When.DEFAULT_DATETIME_FORMAT  # --datetime-format

            print()
            print(datetime.datetime.now().strftime(date_format))

    @staticmethod
    def print_month(date: datetime.date) -> None:
        """
        Prints the current month.

        :param date: Current date.
        """
        month = calendar.month(date.year, date.month).splitlines()

        # Print the year header and the days of the week.
        print(month[0])
        print(month[1])

        # Print the weeks highlighting the current day of the month.
        day = f"{date.day:>2}"
        found_day = False

        for data in month[2:]:
            if not found_day and day in data:
                data = data.replace(day, When.reverse_color(day))
                found_day = True

            print(data)

    @staticmethod
    def print_quarter(date: datetime.date) -> None:
        """
        Prints all the months in the current quarter.

        :param date: Current date.
        """
        month_name = calendar.month_name[date.month]
        quarter = When.get_calendar_quarter(date)
        year = calendar.calendar(date.year).splitlines()

        # Print the year header.
        print(year[0])
        print()

        # Find the current quarter.
        quarter_start = 2

        for line in year[quarter_start:]:
            if month_name in line:
                break

            quarter_start += 1

        # Highlight the current month name.
        year[quarter_start] = year[quarter_start].replace(month_name, When.reverse_color(month_name))

        # Print the month names and weekdays.
        print(year[quarter_start])
        print(year[quarter_start + 1])

        # Print the weeks highlighting the current day of the current month.
        day = f"{date.day:>2}"
        found_day = False

        for data in year[quarter_start + 2:]:
            if not data:  # End of quarter?
                break

            if not found_day and day in data[quarter.start:quarter.end]:
                data = When.color_day_in_week(day, data, quarter)
                found_day = True

            print(data)

    @staticmethod
    def print_year(date: datetime.date) -> None:
        """
        Prints all the months in the current year.

        :param date: Current date.
        """
        month_name = calendar.month_name[date.month]
        quarter = When.get_calendar_quarter(date)
        year = calendar.calendar(date.year).splitlines()

        # Print the months highlighting the current month and the current day.
        day = f"{date.day:>2}"
        found_day, found_month = False, False

        for data in year:
            if not found_month and month_name in data:
                data = data.replace(month_name, When.reverse_color(month_name))
                found_month = True

            if not found_day and found_month and day in data[quarter.start:quarter.end]:
                data = When.color_day_in_week(day, data, quarter)
                found_day = True

            print(data)

    @staticmethod
    def reverse_color(value: str) -> str:
        """
        Reverses the color for the value.

        :param value: Value to reverse color for.
        :return: The value with reversed color.
        """
        return f"{colors.REVERSE}{value}{colors.RESET}"

    def validate_parsed_arguments(self) -> None:
        """
        Validates the parsed command-line arguments.
        :return: None
        """
        pass


if __name__ == "__main__":
    When().run()
