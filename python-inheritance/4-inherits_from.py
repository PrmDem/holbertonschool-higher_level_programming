#!/usr/bin/python3

"""Example case:
    >>> obj = False
    >>> inherits_fr*m(obj, int)
    True inherited fr*m class int
    """


def inherits_from(obj, a_class):
    """checks if obj is an instance
        of a subclass of a_class

    Args:
        obj (any): variable to check the class of
        a_class: class we want to check in relation to obj's class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
