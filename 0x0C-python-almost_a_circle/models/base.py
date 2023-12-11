#!/usr/bin/python3
'''class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all classes and
      to avoid duplicating the same code'''
from json import dumps, loads

class Base:
    ''' bass class to to avoid dublication.'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
