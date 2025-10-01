#!/usr/bin/python3

""" Uses the `json.loads()` method to deserialize
    a Python object from a JSON-formatted string.
"""
import json


def from_json_string(my_str):
    """Returns the Python representation of an object (string).

    Args:
        my_obj (str): The JSON string.

    Returns:
        str: The Python string representation of the object.
    """
    return json.loads(my_str)
