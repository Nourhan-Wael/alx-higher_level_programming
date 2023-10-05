#!/usr/bin/python3
def pow(a, b):
    j = a
    i = 1
    if b > 0:
        while i < b:
            j *= a
            i = i + 1
    elif b < 0:
        i = 0
        while i >= b:
            j /= a
            i = i - 1
    return (j)
