#!/usr/bin/python3
"""Module that defines a text file-reading function."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
