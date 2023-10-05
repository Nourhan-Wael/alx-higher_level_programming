#!/usr/bin/python3
def uppercase(str):
    cn = 0
    for i in str:
        j = 0
        cn = cn + 1
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            j = ord(i) - 32
        else:
            j = ord(i)
        if (cn == len(str)):
            print("{:c}".format(j))
        else:
            print("{:c}".format(j), end="")
