#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_ToF = my_list[:]
    for int in my_list:
        if my_list[int] % 2 == 0:
            list_ToF[int] = True
        else:
            list_ToF[int] = False
    return list_ToF
