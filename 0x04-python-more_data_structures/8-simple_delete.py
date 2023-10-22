#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    i = 0
    k = list(a_dictionary.keys())
    while i < len(k):
        if k[i] == key:
            del a_dictionary[key]
        i += 1
    return a_dictionary
