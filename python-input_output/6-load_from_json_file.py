#!/usr/bin/python3

"""Creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Load data from a JSON file.

    Opens the specified JSON file, reads its contents using UTF-8-SIG encoding,
    and returns the deserialized Python object.

    Args:
        filename (str): The path to the JSON file to be loaded.

    Returns:
        Any: The Python object resulting from the JSON deserialization.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file does not contain valid JSON.
    """
    with open(filename, 'r', encoding="utf-8-sig") as f:
        data = json.load(f)
    return data
