#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 1
my_rectangle.__width = 20
my_rectangle.x = 4
print(my_rectangle.__dict__)
