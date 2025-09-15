#!/usr/bin/python3

"""This module uses user-provided 'size'
    to print the character '#' in a square shape.

    Example:
    >>> square(3)
    ###
    ###
    ###
"""


class Square:
    """Contains all attributes of a Square
    Printed with character '#'
    """

    def __init__(self, size=0):
        """
        Instantiates a square of size 'size'

        Args:
            size (int): width and height for square
        """
        self.__size = size

    @property
    def size(self):
        """gets size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """allows size to be set by user input"""
        if not isinstance(value, int):
            """TypeError: raised if passed size is not an int"""
            raise TypeError("size must be an integer")
        if value < 0:
            """ValueError: raised if passed size is inferior to 0"""
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns
           area of the square
        """
        return self.__size * self.__size
