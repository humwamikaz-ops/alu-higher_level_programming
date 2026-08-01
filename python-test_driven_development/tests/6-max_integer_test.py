#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function"""

    def test_normal_list(self):
        """Tests a normal ascending list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Tests an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Tests a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Tests an empty list returns None"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Tests a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_all_same(self):
        """Tests a list where all elements are equal"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """Tests a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
