#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_x = matrix.copy()
    for i in range(len(new_x)):
        new_x[i] = list(map(lambda x: x ** 2, new_x[i]))
    return new_x
