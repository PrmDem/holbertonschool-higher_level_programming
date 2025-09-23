#!/usr/bin/python3

"""Holds class BaseGeometry
    and public instance method 'area'
    """


class BaseGeometry:
    """Doesn't contain much other than an unset Area method"""
    def area(self):
        """Raises an exception when user tries to use 'area'"""
        raise Exception("area() is not implemented")
