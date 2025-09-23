#!/usr/bin/python3

"""Holds class BaseGeometry
    where we don't determine an area
    but we do determine whether a variable is
        an int > 0
    """


class BaseGeometry:
    """Doesn't contain much other than an unset Area method"""
    def area(self):
        """Raises an exception when user tries to use 'area'"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ensures value is an integer > 0

        Args:
            name (string): name given to the variable
            value (int): value of the variable 'name'
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
