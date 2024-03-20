#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for n in range(len(my_list)):
        if my_list[n] == search:
            newlist.append(replace)
        else:
            newlist.append(my_list[n])
    return newlist
