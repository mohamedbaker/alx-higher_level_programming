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

    def integer_validator(self, name, value):
        '''validates positve int'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
