#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 2, 9999999, 3 , 6 , 7, 99, 0]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
