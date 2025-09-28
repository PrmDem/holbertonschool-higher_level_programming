#!/usr/bin/python3

"""Checks whether an object is a direct subclass
    of the one passed as argument
"""


def inherits_from(obj, a_class):
    """checks if obj is an instance
        of a subclass of a_class

    Args:
        obj (any): variable to check the class of
        a_class: class we want to check in relation to obj's class

    Returns:
        True if is subclass
        False if not
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
