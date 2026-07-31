#!/usr/bin/python3
"""Module that defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization."""
    return obj.__dict__
