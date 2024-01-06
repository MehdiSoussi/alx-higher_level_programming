#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print()
        return None
    for i in matrix:
        lengthy = len(i)
        for j in range(lengthy):
            if j != lengthy - 1:
                print("{:d} ".format(i[j]), end="")
            else:
                print("{:d}".format(i[j]))
