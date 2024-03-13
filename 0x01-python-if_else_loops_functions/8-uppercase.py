#!/usr/bin/python3
def uppercase(str):
    A = ord('A')
    Z = ord('Z') + 1
    n1 = ord('1')
    n2 = ord('9') + 1
    s1 = ord(" ")
    s2 = ord("/")
    upperconv = ord('a') - ord('A')
    newstring = []
    i = 0
    for c in str:
        if ord(c) in range(A, Z) or ord(c) in range(s1, s2) or ord(c) in range(n1, n2):
            newstring.append(c)
        else:
            i = ord(c) - upperconv
            newstring.append("{:c}".format(i))
    new_string = "".join(newstring)
    print(new_string)
