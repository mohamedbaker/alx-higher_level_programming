#!/usr/bin/python3
'''Module for sqaure cls. '''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''sqaure cls extends from Rectangle.'''
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor '''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' overrid str and return str foramt for sqr'''
        return ("[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                              self.id, self.x, self.y,
                                              self.width))

    @property
    def size(self):
        ''' getter for the sqr size.'''
        return self.width

    @size.setter
    def size(self, new_side):
        ''' setter for size'''
        self.width = new_side
        self.height = new_side

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
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        ''' Return the dictionary repr of Square. '''
        return ({'id': getattr(self, "id"),
                 'size': getattr(self, "width"),
                 'x': getattr(self, "x"),
                 'y': getattr(self, "y")})
