#!/usr/bin/python3

"""Further builds on class 'List'."""


class MyList(list):
    """contains class methods
       building up on original list class
    """

    def print_sorted(self):
        """prints list items in ascending order"""
        print(sorted(self))
