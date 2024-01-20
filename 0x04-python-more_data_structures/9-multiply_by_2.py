#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_copy = a_dictionary.copy()
    for key, value in dic_copy.items():
        dic_copy[key] = value * 2
    return dic_copy
