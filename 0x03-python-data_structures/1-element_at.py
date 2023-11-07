#!/usr/bin/python3
"""
function that retrieves an element from a list like in C using index.
If idx is negative, the function should return None.
f idx is out of range, the function should return None.
"""


def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list):
        return
    else:
        return my_list[idx]
