#!/usr/bin/python3
'''look up module.'''


def lookup(obj):
    '''
       looks up available attributes and methods of an object.
       args:
            obj : object to look up for.
        Returns:
                 the list of available attributes and methods of an object
    '''

    return (list[dir(obj)])
