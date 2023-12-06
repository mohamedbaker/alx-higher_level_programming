#!/usr/bin/python3
"""Module  Python class-to-JSON function."""


def class_to_json(obj):
    """function that returns the dictionary desc with simple data structure """
    return obj.__dict__
