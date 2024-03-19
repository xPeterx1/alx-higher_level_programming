#!/usr/bin/python3
def max_integer(my_list=[]):
    list_len = len(my_list)
    if list_len == 0:
        return "None"
    max = 0
    for i in my_list:
        if max < i:
            max = i
    return (max)
