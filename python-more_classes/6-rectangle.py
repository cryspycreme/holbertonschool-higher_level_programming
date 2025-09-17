#!/usr/bin/python3

"""
A function that creates a Class called Rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if (self.height == 0) or (self.width == 0):
            return ""
        else:
            return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """
    Define instance attributes width, height
    """

    # width attribute
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # height attribute
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height == 0) or (self.width == 0):
            return 0
        else:
            return (self.height * 2) + (self.width * 2)
