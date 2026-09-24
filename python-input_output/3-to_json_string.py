#!/usr/bin/python3
"""Module that defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
