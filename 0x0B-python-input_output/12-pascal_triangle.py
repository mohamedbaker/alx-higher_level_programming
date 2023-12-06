#!/usr/bin/python3
"""Defines a Pascal's triangle function."""


def pascal_triangle(n):
    """Represent Pascal's tringle with size n.

       Return:  list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    rows = [[1]]
    while len(rows) != n:
        row = rows[-1]
        tmp = [1]
        for i in range(len(row) - 1):
            tmp.append(row[i] + row[i + 1])
        tmp.append(1)
        rows.append(tmp)
    return rows
