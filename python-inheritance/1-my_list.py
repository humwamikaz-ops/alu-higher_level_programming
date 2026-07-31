#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Implements sorted printing for a built-in list sub-class."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
