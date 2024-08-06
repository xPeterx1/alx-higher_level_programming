#!/usr/bin/python3
"""Module 0-rectangle
The module defines """


class Rectangle:
    """hello"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """constructor"""
        Rectangle.number_of_instances += 1
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
            return (length + width)
        return (0)

    def __str__(self):
        """print square"""
        if self.height and self.width:
            for i in range(self.height):
                for j in range(self.width):
                    print('#', end="")
                if (i == (self.height - 1)):
                    return ("")
                print()

        else:
            return ("")

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
