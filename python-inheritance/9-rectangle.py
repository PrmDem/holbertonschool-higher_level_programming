#!/usr/bin/python3

"""Holds class BaseGeometry
    where we don't determine an area
    but we do determine whether a variable is
        an int > 0

    Holds subclass Rectangle
    """


class BaseGeometry:
    """Contains unset area method with raised exception,
    and integer_validator method to check the values passed."""
    def area(self):
        """calculates the area of our shape"""
        return self._Rectangle__width * self._Rectangle__height

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
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """instantiates a rectangle using height and width"""
    def __init__(self, width, height):
        """initialises an instance of Rectangle

        Args:
            width (int): sets width value of our Rectangle instance
            height (int): sets height value of our Rectangle instance
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        """returns a string representation
        of the rectangle like so:

        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
