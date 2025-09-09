#!/usr/bin/python3

def max_integer(my_list=[]):
    max = 0
    if my_list:
        for int in my_list:
            if int > max:
                max = int
        return max
    else:
        return None
