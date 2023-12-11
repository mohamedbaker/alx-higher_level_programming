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

    @properaty
    def size(self):
        ''' getter for the sqr size.'''
        return self.width

    @size.setter
    def size(self, new_side):
        ''' setter for size'''
        self.width = new_side
        self.height = new_side
