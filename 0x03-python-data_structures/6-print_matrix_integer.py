#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        print()
        return None
    for i in matrix:
        l = len(i)
        for j in range(l):
            if j != l - 1:
                print("{:d} ".format(i[j]), end="")
            else:
                print("{:d}".format(i[j]))

