#!/usr/bin/python3
"""Defines inherited list  MyList."""


class MyList(list):
    """sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted asc. order."""
        print(sorted(self))
