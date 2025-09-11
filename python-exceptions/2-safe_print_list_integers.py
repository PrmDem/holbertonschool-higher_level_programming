#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            if not isinstance(my_list[i], int):
                continue
            else:
                print("{}" .format(my_list[i]), end='')
                count += 1
        except IndexError:
            print("IndexError: list index out of range")
            break
    print()
    return count
