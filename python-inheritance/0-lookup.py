#!/usr/bin/python3

"""returns available attributes
   & methods of an object
   as a list"""


def lookup(obj):
    """
    Args:
        obj (object): can be anything

    Returns:
        list: contains attributes & methods
    """
    return list(dir(obj))
