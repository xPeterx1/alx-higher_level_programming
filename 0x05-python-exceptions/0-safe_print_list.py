#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        for element in new_list:
            print(element, end="")
        print()
        return x
    except IndexError:
        count = 0
        for x in my_list:
            print(x, end="")
            count+=1
        print()
        return count
