#!/usr/bin/python3

"""This module defines a class 'square'
    and gives it the attribute 'size',
    which is provided by the user.
"""


class Square:
    """Contains all attributes of a Square
    Printed with character '#'
    """

    def __init__(self, size):
        """
        Instantiates a square of size 'size'

        Args:
            size (int): width and height for square
        """
        self.__size = size
