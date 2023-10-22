#!/usr/bin/python3
def best_score(a_dictionary):
    mx = 0
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > mx:
            mx = a_dictionary[i]
            k = i
    return k
