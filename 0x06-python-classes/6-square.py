#!/usr/bin/python3
"""Square Module"""


class Square:
    """Square Definition."""

    def __init__(self, size=0, position=(0, 0)):
        """constructor.

        Args:
            size: size of square side
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or 
             not all(isinstance(i, int) for i in value) or 
               not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the square area
        Returns:
            Square area
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints the square."""
        for x in range(self.__position[1]):
            print()
        for y in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
        else:
            print()
