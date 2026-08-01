#!/usr/bin/python3
"""Unittests for the Square class."""
import unittest
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square initialization."""

    def test_basic_init(self):
        """Tests width and height equal size."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_full_init(self):
        """Tests all attributes assigned correctly."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_validation_inherited(self):
        """Tests that width validation from Rectangle applies."""
        with self.assertRaises(ValueError):
            Square(-5)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str(self):
        """Tests the string representation format."""
        s = Square(5, 2, 1)
        self.assertEqual(str(s), "[Square] ({}) 2/1 - 5".format(s.id))


class TestSquareSize(unittest.TestCase):
    """Tests for Square's size getter/setter."""

    def test_size_getter(self):
        """Tests size returns the current width."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        """Tests setting size updates both width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_setter_invalid(self):
        """Tests invalid size raises TypeError."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with args."""

    def test_update_all_args(self):
        """Tests updating all attributes via args."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with kwargs."""

    def test_update_kwargs(self):
        """Tests updating attributes via keyword arguments."""
        s = Square(5)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_to_dictionary(self):
        """Tests the dictionary representation contains the right keys."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(d, {"id": s.id, "size": 10, "x": 2, "y": 1})


if __name__ == "__main__":
    unittest.main()
