#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        if len(row) == 0:
            print()
        for elem in row:
            print("{:d}".format(elem),
                  end=" " if elem != row[-1] else '\n')
