#!/usr/bin/python3
import json

"""Writes an Object to a text file
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.

    Serializes the given Python object and saves it
            to a file using UTF-8 encoding.

    Args:
        my_obj (any): The Python object to serialize and write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
