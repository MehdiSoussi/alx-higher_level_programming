#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_todelete = []
    for key, val in a_dictionary.items():
        if val == value:
            list_todelete.append(key)
    for x in list_todelete:
        list_todelete.pop(x)
