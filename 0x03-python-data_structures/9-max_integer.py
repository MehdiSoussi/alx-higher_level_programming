#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max = 0
        for x in my_list:
            if max < x:
                max = x
        return max
