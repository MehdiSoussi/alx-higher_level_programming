#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    commonality = []
    for x in set_1:
        if x not in set_2:
            commonality.append(x)
    for x in set_2:
        if x not in set_1:
            commonality.append(x)
    return set(commonality)
