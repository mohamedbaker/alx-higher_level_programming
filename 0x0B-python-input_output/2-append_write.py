#!/usr/bin/python3
"""appends a string to txt file."""


def append_write(filename="", text=""):
    """
       Function that appends a string at the end of a text file (UTF8)
       Return: the number of characters added:
    """
    with open(filename, 'a+', encoding="UTF-8") as f:
        return (f.write(text))
        f.close()
