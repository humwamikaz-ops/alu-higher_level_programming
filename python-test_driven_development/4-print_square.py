#!/usr/bin/python3
"""Module that prints a square using the # character."""


def print_square(size):
    """Prints a square of size length using the # character.

    Args:
        size (int): the size length of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
