#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resList = []
    for idx in range(0, list_length):
        try:
            isinstance((my_list_1[idx], my_list_2[idx]), (int, float))
            res = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            res = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            res = 0
            continue
        except IndexError:
            print("out of range")
            res = 0
            continue
        finally:
            resList.append(res)
    return resList
