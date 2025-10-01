#!/usr/bin/python3

"""Prints the contents of a file
    line by line
"""


def read_file(filename=""):
    """parses through a file and prints it

    Args:
        filename: name of the file to open

    Returns number of bytes read."""

    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
