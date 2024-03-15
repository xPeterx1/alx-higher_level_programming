#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    i = 0
    symbols = ["+", "-", "*", "/"]
    addresult = add(a, b)
    subresult = sub(a, b)
    mulresult = mul(a, b)
    divresult = div(a, b)
    values = [addresult, subresult, mulresult, divresult]
    for c in symbols:
        print("{} {} {} = {}".format(a, c, b, values[i]))
        i += 1
