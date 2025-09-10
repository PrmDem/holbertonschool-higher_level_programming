#!/usr/bin/python3
def roman_to_int(roman_string):
    correspondances = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
    numList = []
    res = 0
    init = 0
    next = 1
    for letter in roman_string:
        for key, value in correspondances.items():
            if letter == key:
                numList.append(value)
    if len(numList) == 1:
        res = numList[0]
    else:
        while init < (len(numList) - 1) and next <= (len(numList) - 1):
            if numList[init] < numList[next]:
                res -= numList[init]
            elif numList[init] >= numList[next]:
                res += numList[init]
            init += 1
            next += 1
        res += numList[init]
    return res
