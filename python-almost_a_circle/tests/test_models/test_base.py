#!/usr/bin/python3
"""Unittest module for models/base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_explicit_assignment(self):
        """Test passing explicit ID value."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_mixed_assignment(self):
        """Test mixing auto-increment and explicit IDs."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_id_negative(self):
        """Test passing negative ID."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_zero(self):
        """Test passing zero as ID."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_string(self):
        """Test passing string as ID."""
        b = Base("12")
        self.assertEqual(b.id, "12")


if __name__ == "__main__":
    unittest.main()
