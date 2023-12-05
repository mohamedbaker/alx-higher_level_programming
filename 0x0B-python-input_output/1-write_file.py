#!/usr/bin/python3
""" module for writing in txt file """


def write_file(filename="", text=""):
    """
         function that writes a string to a text file (UTF8)
         return: the number of characters written
    """
    with open(filename, 'w', encoding="UTF-8") as f:
        return(f.write(text))
        f.close()
