#!/usr/bin/python3

"""This module adds arguments to a Python list,
    then saves it to a .json file

    It employs the modules json, sys, fileinput
    as well as the save_to_json_file and
    load_from_json_file functions from earlier tasks.

    Exemple use:
    >>> 7-add_item.py This is a test
    >>> cat add_item.json ; echo ""
    ["This", "is", "a", "test"]
"""

import os.path
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':

    filename = "add_item.json"

    if os.path.exists("./add_item.json"):
        my_list = list(load_from_json_file(filename))
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)
