#!/usr/bin/python3
def uniq_add(my_list=[]):
    flag = False
    sum = 0
    i = 0
    if len(my_list) == 0:
        return 0
    if len(my_list) == 1:
        return my_list[0]
    while i < len(my_list):
        j = i + 1
        while j < len(my_list):
            if my_list[i] == my_list[j]:
                my_list.pop(j)
            j += 1
        i += 1
    if my_list[0] == my_list[1]:
        my_list.pop(1)
    for k in my_list:
        sum += k
    return sum
