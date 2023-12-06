#!/usr/bin/python3
"""module student class."""


class Student:
    """Student Representation."""

    def __init__(self, first_name, last_name, age):
        """constructor for new Student.

        Args:
            first_name (str): first name of the student.
            last_name (str):  last name of the student.
            age (int):  age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of  Student."""
        try:
            for ele in attrs:
                if type(ele) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        newDict = dict()
        for k, val in slef.__dict__.items():
            if k in attrs:
                newDict[k] = val
        return new_dict
