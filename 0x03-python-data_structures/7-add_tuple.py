#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    final_tuple = ()
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    final_tuple = a[0] + b[0], a[1] + b[1]
    return final_tuple
