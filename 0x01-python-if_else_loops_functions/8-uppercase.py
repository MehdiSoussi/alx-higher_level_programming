#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        asc = ord(c)
        if asc >= 97 and asc <= 122:
            print(chr(asc - 32), end="")
        else:
            print(c, end="")
    print()
