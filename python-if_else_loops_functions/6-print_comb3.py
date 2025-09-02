#!/usr/bin/python3
for diz in range(0, 9):
    for unit in range(diz + 1, 10):
        if unit != diz:
            if diz == 8 and unit == 9:
                print("{}{}" .format(diz, unit))
            else:
                print("{}{}" .format(diz, unit), end=', ')
        unit += 1
    diz += 1
