#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_all_positive(self):
        self.assertEqual(max_integer([1, 5, 10, 15, 20]), 20)

    def test_all_negative(self):
        self.assertEqual(max_integer([-4, -7, -1, -8, -16]), -1)

    def test_any_value(self):
        self.assertEqual(max_integer([12, -5, 9, 78, -45]), 78)

    def test_same_number(self):
        self.assertEqual(max_integer([5, 5, 5, 5, 5]), 5)

    def test_one_number(self):
        self.assertEqual(max_integer([9]), 9)

    def test_empty_list(self):
        self.assertEqual(max_integer(), None)
