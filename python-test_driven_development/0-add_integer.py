#!/usr/bin/python3
"""Module that adds two integers together."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int/float): first number.
        b (int/float): second number, defaults to 98.

    Returns:
        int: the sum of a and b, cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
