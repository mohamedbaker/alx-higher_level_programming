#!/usr/bin/python3
""" Module Reading file. """


def read_file(filename=""):
    """  function that reads a text file (UTF8) and prints it to stdout."""
    with open(filename, 'r', encoding = "UTF-8") as f:
      readData = f.read()
      print(readData)
      f.close()
