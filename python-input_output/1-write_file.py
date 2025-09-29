#!/usr/bin/python3

"""Python module using I/O to:
    - write to a file, creating it if
        nonexistent
    - print the contents of the file
        to stdout
"""


def write_file(filename="", text=""):
    """Writes to file then prints it

    Args:
        filename (str): name of file to write to.
                Defaults to none
        text (str): string to write to file.
                Defaults to none

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        written_data = f.write(text)
        return written_data
