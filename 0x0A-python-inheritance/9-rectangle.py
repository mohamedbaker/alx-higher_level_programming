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


class Rectangle(BaseGeometry):
    '''represents a rectangle.'''
    def __init__(self, width, height):
        '''init.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
