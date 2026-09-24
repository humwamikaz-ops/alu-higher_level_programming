#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represents base geometry."""

    def area(self):
        """Raises an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
