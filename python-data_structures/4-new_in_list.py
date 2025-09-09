#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newList = my_list[:]
    if idx > (len(my_list) - 1) or idx < 0:
        return my_list
    else:
        newList[idx] = element
        return newList
