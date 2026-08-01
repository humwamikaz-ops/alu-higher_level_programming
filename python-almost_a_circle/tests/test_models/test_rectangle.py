#!/usr/bin/python3
"""Unittest module for models/rectangle.py."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test suite for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_inheritance(self):
        """Test that Rectangle inherits from Base."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_rectangle_valid_instantiation(self):
        """Test valid instantiation of Rectangle."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 12)

    # --- Type Errors ---

    def test_type_error_width(self):
        """Test TypeError for non-integer width."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10], 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 2)

    def test_type_error_height(self):
        """Test TypeError for non-integer height."""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, None)

    def test_type_error_x(self):
        """Test TypeError for non-integer x."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, 2.5)

    def test_type_error_y(self):
        """Test TypeError for non-integer y."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, "4")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 0, True)

    # --- Value Errors ---

    def test_value_error_width(self):
        """Test ValueError for width <= 0."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_value_error_height(self):
        """Test ValueError for height <= 0."""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_value_error_x(self):
        """Test ValueError for x < 0."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_value_error_y(self):
        """Test ValueError for y < 0."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)


if __name__ == "__main__":
    unittest.main()
