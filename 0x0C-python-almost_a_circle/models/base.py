#!/usr/bin/python3
'''class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all classes and
      to avoid duplicating the same code'''


class Base:
    ''' bass class to to avoid dublication.'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
