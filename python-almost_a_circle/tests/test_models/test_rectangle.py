#!/usr/bin/python3
"""Unittest module for models/rectangle.py."""
import unittest
import io
import sys
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON files after tests."""
        for filename in ["Rectangle.json", "Square.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_rectangle_instantiation(self):
        """Test valid instantiation of Rectangle."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        r2 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r2.id, 12)

    def test_rectangle_zero_height(self):
        """Test Rectangle(1, 0) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_type_errors(self):
        """Test invalid attribute types."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        """Test invalid attribute values."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_display_without_x_and_y(self):
        """Test display() without x and y."""
        r = Rectangle(2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_display_without_y(self):
        """Test display() without y."""
        r = Rectangle(2, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  ##\n  ##\n")

    def test_display(self):
        """Test display() with x and y."""
        r = Rectangle(2, 3, 2, 2)
        output = io.StringIO()
        sys.stdout = output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update method with *args."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=1, width=2, x=3, y=4, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 2/1")

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        res = r.to_dictionary()
        expected = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        self.assertEqual(res, expected)

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None)."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test Rectangle.save_to_file([])."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_rectangle_list(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)])."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        res = Rectangle.load_from_file()
        self.assertEqual(res, [])

    def test_load_from_file_exists(self):
        """Test Rectangle.load_from_file() when file exists."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
