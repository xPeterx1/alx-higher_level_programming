#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    result = 0
    for i in newlist:
        result += i
    return result
