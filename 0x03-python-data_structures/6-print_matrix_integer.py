#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for i in range(len(matrix)):
            if len(matrix[0]) > 1:
                for j in range(len(matrix[0]) - 1):
                     print("{:d}".format(matrix[i][j]), end=" ")
                print("{:d}".format(matrix[i][j + 1]), end="")
            else:
                print("{:d}".format(matrix[i][0]), end="")
            print()
    else:
        print()
