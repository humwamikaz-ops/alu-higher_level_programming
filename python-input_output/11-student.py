#!/usr/bin/python3
"""Module that defines a Student class with reload capabilities."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names (strings) to
                retrieve. Defaults to None.

        Returns:
            dict: Dictionary representation containing selected or all
            attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(element, str) for element in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary.

        Args:
            json (dict): Key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
