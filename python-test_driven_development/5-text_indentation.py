#!/usr/bin/python3

"""Replaces characters '.:?' in text by two new lines.

Each line of output will not start or end with a space,
even if the original text contains extra spaces around those characters.

Parameters:
    text (str): The text to be processed and printed.

Known issues:
    Because lstrip() does not work,
    Replacing 'char + " "' means that an ending period
    with no whitespace after it, will not be replaced by new lines.
"""


def text_indentation(text):
    """breaks provided text 
    by adding new lines at specific signs

    Args:
        text (str): text to indent

    Raises:
        TypeError: should the provided 'text' arg not be a string
    """
    if not isinstance(text, str):
        # ensures text is a string
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char + " ", char + "\n\n")
        # removes white space, inserts two new lines

    print(text)
