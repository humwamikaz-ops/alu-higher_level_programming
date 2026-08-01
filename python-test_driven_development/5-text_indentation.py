#!/usr/bin/python3
"""Module that prints text with indentation after ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after ., ? and :

    Args:
        text (str): the text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    special_chars = ".?:"
    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in special_chars:
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
