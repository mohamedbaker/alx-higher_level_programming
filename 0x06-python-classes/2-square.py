#!/usr/bin/python3
"""Square module"""


class Square:
    """square definition
    Attr:
        __size: size of square side
    """
    def __init__(self, size=0):
        """init square
        Args:
            size: size of square side
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
