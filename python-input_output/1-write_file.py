#!/usr/bin/python3
"""Module that defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file and returns characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
