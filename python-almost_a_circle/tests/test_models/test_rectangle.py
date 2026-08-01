#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle initialization."""

    def test_basic_init(self):
        """Tests width and height are assigned correctly."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_full_init(self):
        """Tests all attributes assigned with an explicit id."""
        r = Rectangle(10, 2, 1, 2, 12)
        self.assertEqual(r.id, 12)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_auto_id(self):
        """Tests id auto-increments when not given."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, r1.id + 1)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int(self):
        """Tests width as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_height_not_int(self):
        """Tests height as a string raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_width_negative(self):
        """Tests negative width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_width_zero(self):
        """Tests zero width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_negative(self):
        """Tests negative height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_not_int(self):
        """Tests x as a dict raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, x={})

    def test_x_negative(self):
        """Tests negative x raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """Tests negative y raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_setter_width(self):
        """Tests setting width after instantiation."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = -10


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area(self):
        """Tests area calculation."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_with_position(self):
        """Tests area is unaffected by x/y."""
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str(self):
        """Tests the string representation format."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with args."""

    def test_update_id(self):
        """Tests updating only id."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_all_args(self):
        """Tests updating all attributes via args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with kwargs."""

    def test_update_kwargs(self):
        """Tests updating attributes via keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_multiple(self):
        """Tests updating multiple attributes via keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/10")


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_to_dictionary(self):
        """Tests the dictionary representation contains the right keys."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d, {"id": r.id, "width": 10,
                              "height": 2, "x": 1, "y": 9})

    def test_to_dictionary_type(self):
        """Tests the return type is dict."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)


if __name__ == "__main__":
    unittest.main()
