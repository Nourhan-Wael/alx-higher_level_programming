#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for i in keys:
        print("{0}: {1}".format(i, a_dictionary[i]))
