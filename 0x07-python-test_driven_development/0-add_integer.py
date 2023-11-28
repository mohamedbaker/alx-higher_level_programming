#!/usr/bin/python3
''' addition func integers '''


def add_integer(a, b=98):
    ''' add two ints a and b , result (int)

        float args to be converted to int before add.

        Raises:
               TypeError: if either a or b is non_int or non_float
    '''

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError('a must be an integer')

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError('b must be an integer')

    return a + b
