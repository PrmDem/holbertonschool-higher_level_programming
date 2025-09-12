#!/usr/bin/python3

"""
    Adds two numbers after ensuring they are integers or floats.
    Should they be floats, they are cast as int
            at the time of the addition
    Returns: result of a + b as an int"""


def add_integer(a, b=98):
    """a, b (int, float) where b is optional, defaults to 98
    both are type-tested before use
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
