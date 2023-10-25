#!/usr/bin/python3
"""square module."""


class Square:
    """square module."""
    def __init__(self, size=0):
        """constructor
        Args:
            size: length
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """area
        returns:
            the area
        """
        return self.__size ** 2
