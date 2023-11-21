#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square Definition."""

    def __init__(self, size=0):
        """constructor.

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

    def area(self):
        """Calculates the square area
        Returns:
            Square are
        """
        return (self.__size) ** 2
