#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorteddic = sorted(a_dictionary)
    for i in sorteddic:
        print("{:s}: {}".format(i, a_dictionary[i]))
