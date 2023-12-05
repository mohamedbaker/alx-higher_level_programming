#!/usr/bin/python3
'''
BaseGeometry Class
'''


class BaseGeometry:
    '''base geo class
       raises: (exception)
    '''
    def area(self):
        ''' area methode
            raises: (exception): with the message area() is not implemented
        '''
        raise Exception("area() is not implemented")
