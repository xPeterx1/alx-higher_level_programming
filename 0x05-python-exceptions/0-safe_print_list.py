def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        for x in new_list:
            print(x, end="")
        print()
        return x
    except IndexError:
        for x in my_list:
            print(x, end="")
        print()
        return x
