#!/usr/bin/python3
''' module checking if obj is instance for same class or not'''


def inherits_from(obj, a_class):
    ''' method checks if obj is instance for same class
        Return : true if obj is instnce otherwise false.
    '''

    return isinstance(obj, a_class)
