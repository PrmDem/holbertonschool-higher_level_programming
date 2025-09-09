#!/usr/bin/python3

def element_at(my_list, idx):
    # gets index of a list element
    # my_list: list to parse
    # idx: index of wanted element
    if idx > len(my_list) or idx < 0:
        return None
    else:
        return my_list[idx]
