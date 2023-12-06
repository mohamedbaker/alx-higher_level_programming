#!/usr/bin/python3
"""module JSON file reading."""
import json


def load_from_json_file(filename):
    """func that creates a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
