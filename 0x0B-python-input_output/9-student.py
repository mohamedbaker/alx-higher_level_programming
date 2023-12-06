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

    def to_json(self):
        """Get a dictionary representation of  Student."""
        return self.__dict__
