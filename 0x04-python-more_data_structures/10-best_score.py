#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max = 0
        keymax = None
        for key, value in a_dictionary.items():
            if value >= max:
                keymax = key
    return keymax
