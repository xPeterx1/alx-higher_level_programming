def islower(c):
    a = ord('a')
    b = ord('z')
    if ord(c) in range(a, b + 1):
        return True
    else:
        return False
