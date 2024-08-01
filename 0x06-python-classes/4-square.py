#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """constructor"""
        if isinstance(size, int):
            if (size < 0):
                raise ValueError('size must be >= 0')
            self.size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """AREA"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
