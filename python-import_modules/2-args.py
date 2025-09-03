#!/usr/bin/python3
from sys import argv
nb_arg = (len(argv) - 1)

if __name__ == '__main__':
    if nb_arg == 1:
        print("1 argument:")
        print("1: {}" .format(argv[1]))
    elif nb_arg == 0:
        print("0 arguments.")
    else:
        print("{} arguments:" .format(nb_arg))
        for i, val in enumerate(argv[1:], start=1):
            print("{}: {}" .format(i, val))
