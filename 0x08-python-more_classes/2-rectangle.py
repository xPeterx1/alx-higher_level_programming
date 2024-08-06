#!/usr/bin/python3
"""Module 0-rectangle
The module defines """


class Rectangle:
    """hello"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    def __getattr__(self, name):
        """getter"""
        return self.__dict__[f"_Rectangle__{name}"]

    def __setattr__(self, name, value):
        """setter"""
        if (name == "width" or name == "height"):
            if isinstance(value, int):
                if value < 0:
                    raise ValueError(f"{name} must be >= 0")
                self.__dict__[f"_Rectangle__{name}"] = value
            else:
                raise TypeError(f"{name} must be an integer")
        self.__dict__[f"_Rectangle__{name}"] = value

    def area(self):
        """area"""
        return (self.width * self.height)

    def perimeter(self):
        """perimeter"""
        length = self.height * 2
        width = self.width * 2
        if (length and width):
            return (lenght + width)
        return (0)
