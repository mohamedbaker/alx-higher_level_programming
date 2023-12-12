#!/usr/bin/python3
'''class will be the “base” of all other classes in this project.
     The goal of it is to manage id attribute in all classes and
      to avoid duplicating the same code'''
from json import dumps, loads
import csv
import turtle
import time
from random import randrange


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
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''write the JSON serialization of a list of objects to a file.'''
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Return list of the JSON string repr.'''

        if json_string is None or json_string == "[]":
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes already set.'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''Return a list of instances from JSON file.'''
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Returns a list of instances from a CSV file.'''
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csv_f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csv_f, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        turtle.Screen().colormode(255)
        for obj in list_rectangles + list_squares:
            n_turtle = turtle.Turtle()
            n_turtle.color((randrange(255), randrange(255), randrange(255)))
            n_turtle.pensize(1)
            n_turtle.penup()
            n_turtle.pendown()
            n_turtle.setpos((obj.x + n_turtle.pos()[0],
                             obj.y - n_turtle.pos()[1]))
            n_turtle.pensize(10)
            n_turtle.forward(obj.width)
            n_turtle.left(90)
            n_turtle.forward(obj.height)
            n_turtle.left(90)
            n_turtle.forward(obj.width)
            n_turtle.left(90)
            n_turtle.forward(obj.height)
            n_turtle.left(90)
            n_turtle.end_fill()

    time.sleep(5)
