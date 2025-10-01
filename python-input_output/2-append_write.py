#!/usr/bin/python3

"""This module, written in Python, uses I/O
    to append a string of text to a file.
"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF-8)
            and returns the number of characters added.

    Opens the file in append mode and writes the specified text to the end.
    If the file does not exist, it will be created.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
