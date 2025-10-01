#!/usr/bin/python3

"""Writes a dictionary to a file
    using JSON representation,
    or deserialises a string representation
    from a given json file
"""
import json


def serialize_and_save_to_file(data, filename):
    """Writes a dict object to a text file using JSON representation.

    Serializes the given Python dictionary and saves it
            to a file using UTF-8 encoding.

    Args:
        data (dict): Python dictionary to serialize and write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load data from a JSON file.

    Opens the specified JSON file, reads its contents using UTF-8-SIG encoding,
    and returns the deserialized Python object.

    Args:
        filename (str): The path to the JSON file to be loaded.

    Returns:
        dict: The Python dictionary from the JSON deserialization.
    """
    with open(filename, 'r', encoding="utf-8-sig") as f:
        return json.load(f)
