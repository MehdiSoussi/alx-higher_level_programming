#!/usr/bin/python3
for n in range(100):
    if n != 89:
        if (n % 10) > (n / 10):
            print("{:02d}, ".format(n), end="")
    else:
        print(n)
