#!/usr/bin/python3
"""Unittest module for models/rectangle.py."""
import unittest
import os
import io
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for Rectangle model."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_rectangle_instantiation(self):
        """Test valid instantiation."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        """Test display method."""
        r = Rectangle(2, 2)
        r.display()
        self.assertEqual(mock_stdout.getvalue(), "##\n##\n")

    def test_str(self):
        """Test str representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        res = r.to_dictionary()
        self.assertEqual(res, {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9})


class TestRectangleSaveToFile(unittest.TestCase):
    """Test save_to_file method of Rectangle class."""

    def tearDown(self):
        """Clean up JSON files."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_save_to_file_None(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_none(self):
        """Test save_to_file with none (lowercase alias)."""
        Rectangle.save_to_file(None)

    def test_save_to_file_empty_list(self):
        """Test save_to_file with empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangles(self):
        """Test save_to_file with list of rectangles."""
        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_one_rectangle(self):
        """Test save_to_file with single rectangle in list."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))


class TestRectangleLoadFromFile(unittest.TestCase):
    """Test load_from_file method of Rectangle class."""

    def tearDown(self):
        """Clean up JSON files."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_load_from_file_no_file(self):
        """Test load_from_file when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test load_from_file when file exists."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)


if __name__ == "__main__":
    unittest.main()
