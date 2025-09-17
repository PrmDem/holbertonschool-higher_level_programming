#!/usr/bin/python3

""" This module creates and prints rectangles
    Well, creates for sure.
    Printing will have to wait.
"""


class Rectangle:
    """ Defines and instantiates rectangles."""

    def __init__(self, width=0, height=0):
        """
        Instantiates a rectangle according to values
        passed by the user.

        Args:
            width (int): defaults to 0, can only be positive
            height (int): defaults to 0, can only be positive
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width for rectangle instantiation
        :value:`int` that sets width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height for rectangle instantiation
        :value:`int` that sets height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2
