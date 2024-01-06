#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        l = len(i)
        for j in range(l):
            if j != l - 1:
                print("{} ".format(i[j]), end="")
            else:
                print("{}".format(i[j]))

