#!/usr/bin/python3
def no_c(my_string):
    if len(my_string) > 0:
        list = []
        list.extend(my_string)
        for i in list:
            if i == 'c' or i == 'C':
                list.remove(i)
        newstring = "".join(list)
        return newstring
