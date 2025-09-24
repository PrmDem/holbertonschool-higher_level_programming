#!/usr/bin/python3

"""Ensures an object is an instance
   of a given class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is
       an instance of a_class,
       False if it isn't.

    Args:
        obj (any): variable to test against a specified class
        a_class: can be any class recognised by Python
   """
    return type(obj) is a_class
