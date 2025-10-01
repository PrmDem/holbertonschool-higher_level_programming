#!/usr/bin/python3

"""Uses the `json.dumps()` method
    to serialize a Python object
    to a JSON-formatted string.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
