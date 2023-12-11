#!/usr/bin/python3
''' module for Rectangle.'''
from models.base import Base


class Rectanglei(Base):
    ''' Rectangle class inhertiting from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self.__width = width
        self._height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, new_x):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, new_y):
        return self.__y
