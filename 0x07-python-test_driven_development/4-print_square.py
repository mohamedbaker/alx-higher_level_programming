#!/usr/bin/python3
"""Module for print_square."""


def print_square(size):
    """Method for presenting a square with # char.
    Args:
        size: size of square.
    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for y in range(size)]
        print("")
