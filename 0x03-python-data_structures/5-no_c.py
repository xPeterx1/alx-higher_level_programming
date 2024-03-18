#!/usr/bin/python3
def no_c(my_string):
    list = []
    nostring = my_string
    list.extend(my_string)
    for i in list:
        if i == 'c' or i == 'C':
            list.remove(i)
    if (len(list) > 0):
        newstring = "".join(list)
        return newstring
    else:
        return nostring
