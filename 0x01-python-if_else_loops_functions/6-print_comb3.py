#!/usr/bin/python3
for n in range(100):
    if n != 89:
        if (n % 10) > (n / 10):
            print(f"{n:02d}, ", end = "")
    else:
        print(n)
