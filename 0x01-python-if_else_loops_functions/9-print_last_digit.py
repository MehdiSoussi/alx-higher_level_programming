#!/usr/bin/python3
def print_last_digit(number):
    if(number > 0):
        r = number % 10
        print(r, end="")
        return r
    else:
        r = (number * -1) % 10
        print(r, end="")
        return r
