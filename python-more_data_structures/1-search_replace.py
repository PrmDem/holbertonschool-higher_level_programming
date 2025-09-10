#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = my_list[:]
    for elem in range(0, len(newList)):
        if newList[elem] == search:
            newList[elem] = replace
    return newList
