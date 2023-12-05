#!/usr/bin/python3
'''Module  Rectangle class base on 7-base geo.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''represents a rectangle.'''
    def __init__(self, width, height):
        '''init.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
