#!/usr/bin/python3

"""Ensures an object is an instance
   of a given class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is
       an instance of a_class or
       one of its subclasses;
       False if it isn't.

    Args:
        obj (any): variable to test against a specified class
        a_class: can be any class recognised by Python
    """
    return isinstance(obj, a_class)
