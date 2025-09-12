#!/usr/bin/python3

"""
Prints a formatted full name.

This function prints the message "My name is <first name> <last name>" where
<first name> and <last name> are the values passed to the function.

Parameters:
    first_name (str): The first name to be printed. Must be a string.
    last_name (str, optional): The last name to be printed. Defaults to an empty string.

Example:
    say_my_name("John", "Doe")
    Output: My name is John Doe

    say_my_name("Alice")
    Output: My name is Alice
"""


def say_my_name(first_name, last_name=""):
    # prints first and last name in a formatted string

    if not first_name:
        raise TypeError("first_name must be a string")
    # Ensures a first_name argument is passed

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Ensures first_name is a string

    if last_name != "":
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    # Ensure last_name, if provided, is a string

    print("My name is {} {}".format(first_name, last_name))
