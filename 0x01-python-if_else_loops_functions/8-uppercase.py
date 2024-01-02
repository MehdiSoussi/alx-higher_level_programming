#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asc = ord(c)
        if asc >= 97 and asc <= 122:
            asc = ord(c) - 32
        print("{:c}".format(asc), end="")
    print()
