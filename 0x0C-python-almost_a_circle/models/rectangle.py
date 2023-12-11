#!/usr/bin/python3
''' module for Rectangle.'''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle class inhertiting from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        ''' property and getter for width. '''
        return self.__width

    @width.setter
    def width(self, new_width):
        ''' setter for width. '''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        return self.__width

    @property
    def height(self):
        ''' property and getter for height. '''
        return self.__height

    @height.setter
    def height(self, new_height):
        '''setter for height. '''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        return self.__height

    @property
    def x(self):
        ''' property and getter for x. '''
        return self.__x

    @x.setter
    def x(self, new_x):
        '''setter for x. '''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        return self.__x

    @property
    def y(self):
        ''' property and getter for y. '''
        return self.__y

    @y.setter
    def y(self, new_y):
        '''setter for y. '''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        return self.__y

    def area(self):
        '''
            returns the area of the Rectangle.
        '''
        return (self.__width * self.__height)

    def display(self):
        ''' dispalys rectangle as # or ""
             depends on x and width and height
         '''
        for v in range(self.y):
            print("")
        for r in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        '''
            returns a string format
        '''
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
