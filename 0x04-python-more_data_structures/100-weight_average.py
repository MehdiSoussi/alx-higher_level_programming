#!/usr/bin/python3
def weight_average(my_list=[]):
    a, b = 0, 0
    for tpl in my_list:
        a += tpl[0] * tpl[1]
        b += tpl[1]
    return a / b
