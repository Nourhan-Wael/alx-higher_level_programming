#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i == ' ':
            print(i, end="")
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{:c}".format(ord(i) - 32), end="")
        else:
            print(i, end="")
    print()
