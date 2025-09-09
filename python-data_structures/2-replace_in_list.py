#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # replaces specific list element
    # my_list: the og list; idx - index of element to replace
    # element: the new value for said element
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        my_list[idx] = element
        return my_list
