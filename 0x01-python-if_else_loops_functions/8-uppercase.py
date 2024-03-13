#!/usr/bin/python3
def uppercase(str):
    a = ord('a')
    z = ord('z')
    for b in str:
        if ord(b) in range(a, z + 1):
            char = chr(ord(b) - 32)
        else:
            char = b
        print("{:s}".format(char), end="")
    print('')
