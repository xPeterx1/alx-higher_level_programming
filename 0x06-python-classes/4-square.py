#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """constructor"""
        self.size = size

    def area(self):
        """AREA"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if isinstance(value, int):
            if (value < 0):
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
        self.__size = value
