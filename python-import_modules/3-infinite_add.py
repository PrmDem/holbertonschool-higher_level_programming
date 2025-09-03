#!/usr/bin/python3
from sys import argv

res = 0
if __name__ == '__main__':
    for item in argv[1:]:
        res += int(item)
    print("{}" .format(res))
