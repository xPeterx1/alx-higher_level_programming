#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    sign = -1
else:
    sign = 1
lastnum = abs(number) % 10
lastnum = lastnum * sign
if lastnum > 5:
    print(f"Last digit of {number} is {lastnum} and is greater than 5")
elif lastnum < 6 and lastnum != 0:
    print(f"Last digit of {number} is {lastnum} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastnum} and is 0")
