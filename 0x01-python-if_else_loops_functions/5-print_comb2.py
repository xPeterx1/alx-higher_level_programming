#!/usr/bin/python3
for b in range(0, 100):
    if b == 99:
        print(b)
    else:
        print("{:0>2d}".format(b), end=", ")
