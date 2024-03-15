#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = 0
    args = sys.argv[1:]
    lenght = len(args)
    if (lenght >= 1):
        print("{} arguments:".format(lenght))
        for i in args:
            print("{}: {} ".format(arg + 1, args[arg]))
            arg += 1
    else:
        print("0 arguments.")
