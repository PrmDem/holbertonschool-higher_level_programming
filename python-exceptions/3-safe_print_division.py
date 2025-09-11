#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        (a, b) != 0
        res = (a / b)
        return res

    except ZeroDivisionError:
        res = None
        return None

    finally:
        print("Inside result: {}".format(res))
