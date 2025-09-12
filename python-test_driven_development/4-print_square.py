#!/usr/bin/python3

"""
Prints a square of the character '#'.

Parameters:
    size (int): The length of each side of the square. Must be positive.

Raises:
    TypeError: If size is not an integer.
    ValueError: If size is negative.

Example:
    >>> print_square(3)
        ###
        ###
        ###
"""


def print_square(size):
    # verifies that size is of type int:
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # verifies that size is a non-zero positive number
    if size < 0:
        raise ValueError("size must be >= 0")

    # prints square of the required size
    for squ in range(0, size):
        print("{}".format('#' * size))
