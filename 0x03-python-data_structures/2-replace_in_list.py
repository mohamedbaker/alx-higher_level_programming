#!/usr/bin/python3
"""
function that replaces an element of a list by idx
If idx is negative, the function should return original list.
f idx is out of range, the function should return original list.
"""


def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
