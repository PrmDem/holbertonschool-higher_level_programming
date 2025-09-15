#!/usr/bin/python3

"""This module uses user-provided 'size'
    to print the character '#' in a square shape.
    It adds white spaces at a position
    provided by the user via the tuple `position`.

    Example:
    >>> square(3)
    ###
    ###
    ###

    >>> square(3, (3, 1))
       ###
       ###
       ###

    Known issue:
        Due to truly confusing instructions,
        the output of my file is different from expectation.
        This will be fixed as soon as I get clarification.
"""


class Square:
    """Contains all attributes of a Square
    Printed with character '#'
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a square of size 'size'

        Args:
            size (int): width and height for square
            position (tuple of ints):
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """gets size of the square
        :value:`int` that sets size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets position at which
           to implement empty spaces

           :value:`tuple of positive integers`
           where x gives a number of empty spaces to print
           and y marks the spot where the spaces are added
           """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for pos in value:
            if not isinstance(pos, int) or pos < 0:
                raise TypeError("position must be a "
                                "tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns
           area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """prints a square of size 'size'
            using character #

            if self.__size == 0,
            prints an empty line
        """

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                if i == self.__position[1]:
                    print(" " * self.__position[0] + "#" * self.__size)
                else:
                    print("#" * self.__size)
