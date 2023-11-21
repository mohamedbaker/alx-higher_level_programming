#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square Definition."""

    def __init__(self, size=0):
        """constructor.

        Args:
            size: size of square side
        """
        self.__size = size

    @property
    def size(self):
        """ Getter Size
        Returns:
            Size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of size
        Args:
            value: square size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """Calculates the square area
        Returns:
            Square are
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints the square."""

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
