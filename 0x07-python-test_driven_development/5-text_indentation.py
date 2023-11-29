#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for adding 2 new lines after '.?:' chars.

    Args:
        text: The str text.

    Raises:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delim = [".", "?", ":"]

    for char in delim:
        text = text.replace(char, char +  "\n\n")
    
    finalText = '\n'.join(line.strip(" ") for line in text.splitlines())


    print(finalText, end = "")
