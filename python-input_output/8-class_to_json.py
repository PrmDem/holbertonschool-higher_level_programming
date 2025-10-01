#!/usr/bin/python3

"""converts an instance of MyClass
    into a json dictionary format
"""


def class_to_json(obj):
    """turn Class Object into json dictionary

    Args:
        obj (any serializable): object of class MyClass

    Returns:
        dictionary description for json serialisation"""
    return (obj.__dict__)
