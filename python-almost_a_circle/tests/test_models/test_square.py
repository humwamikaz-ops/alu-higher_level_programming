#!/usr/bin/python3
"""Unittest module for models/square.py."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suite for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up generated JSON files."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_instantiation(self):
        """Test valid instantiations of Square."""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.size, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_square_invalid_types(self):
        """Test invalid parameter types for Square."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_square_invalid_values(self):
        """Test invalid parameter values for Square."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_square_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_empty(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_square_save_to_file_instance(self):
        """Test Square.save_to_file([Square(1)])."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_square_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        Square.save_to_file([Square(1)])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Square)


if __name__ == "__main__":
    unittest.main()
