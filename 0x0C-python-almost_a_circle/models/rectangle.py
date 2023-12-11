#!/usr/bin/python3
''' module for Rectangle.'''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle class inhertiting from Base class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' property and getter for width. '''
        return self.__width

    @width.setter
    def width(self, new_width):
        ''' setter for width. '''
        if type(new_width) != int:
            raise TypeError("width must be an integer")
        if new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        ''' property and getter for height. '''
        return self.__height

    @height.setter
    def height(self, new_height):
        '''setter for height. '''
        if type(new_height) != int:
            raise TypeError("height must be an integer")
        if new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        ''' property and getter for x. '''
        return self.__x

    @x.setter
    def x(self, new_x):
        '''setter for x. '''
        if type(new_x) != int:
            raise TypeError("x must be an integer")
        if new_x < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_x

    @property
    def y(self):
        ''' property and getter for y. '''
        return self.__y

    @y.setter
    def y(self, new_y):
        '''setter for y. '''
        if type(new_y) != int:
            raise TypeError("y must be an integer")
        if new_y < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_y

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

    def update(self, *args, **kwargs):
        """
            assigns key/value args to attributes
            kwargs is skipped if args is not empty
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        '''return the dictionary represntaion of rectangle. '''
        return ({'x': getattr(self, "x"), 'y': getattr(self, "y"),
                 'id': getattr(self, "id"), 'height': getattr(self, "height"),
                 'width': getattr(self, "width")})
