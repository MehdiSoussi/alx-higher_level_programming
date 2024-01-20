#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def squaring(x):
        return list(map(lambda a: a*a, x))
    return list(map(squaring, matrix))

    #return list(map(lambda x: list(map(lambda a: a*a, x)), matrix))
    #return list(map(lambda x: list(map(lambda a: a*a, x))), matrix)
