#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for number in set(my_list):
        res += number
    return res
