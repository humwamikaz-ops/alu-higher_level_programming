#!/usr/bin/python3
"""Unittests for the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base's id management."""

    def test_id_assigned(self):
        """Tests that a given id is assigned correctly."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_auto_increment(self):
        """Tests that ids auto-increment when not given."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_explicit(self):
        """Tests that passing id=None auto-increments."""
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b2.id, b1.id + 1)


class TestToJsonString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        """Tests None input returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """Tests empty list input returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        """Tests a normal list of dictionaries."""
        list_input = [{"id": 1}]
        result = Base.to_json_string(list_input)
        self.assertEqual(result, '[{"id": 1}]')

    def test_return_type(self):
        """Tests the return type is str."""
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)


class TestFromJsonString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        """Tests None input returns []."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """Tests empty string input returns []."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        """Tests a valid JSON string returns the correct list."""
        json_str = '[{"id": 1}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1}])

    def test_return_type(self):
        """Tests the return type is list."""
        self.assertIsInstance(Base.from_json_string('[{"id": 1}]'), list)


class TestSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        """Removes generated files after each test."""
        try:
            import os
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_save_rectangle_list(self):
        """Tests saving a list of Rectangles produces the right file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)

    def test_save_none(self):
        """Tests saving None writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        """Tests creating a Rectangle from a dictionary."""
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

    def test_create_square(self):
        """Tests creating a Square from a dictionary."""
        s1 = Square(5, 2, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        """Removes generated files after each test."""
        try:
            import os
            os.remove("Rectangle.json")
        except IOError:
            pass

    def test_load_no_file(self):
        """Tests loading when the file doesn't exist returns []."""
        import os
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_after_save(self):
        """Tests loading after saving returns equivalent instances."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(str(loaded[0]), str(r1))


if __name__ == "__main__":
    unittest.main()
