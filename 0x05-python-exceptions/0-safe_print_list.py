#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cn = 0
    try:
        for i in range(0, x):
            print(my_list[i], end="")
            cn+= 1
        print()
    except Exception as e:
        print()
    return cn
