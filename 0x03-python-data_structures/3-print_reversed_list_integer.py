#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list1 = my_list[:]
        my_list1.reverse()
    for i in range(len(my_list1)):
        print("{:d}".format(my_list1[i]))
