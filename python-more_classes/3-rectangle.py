#!/usr/bin/python3

"""
A function that creates a Class called Rectangle
"""


class Rectangle:
    """
    A class that defines a rectangle with width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if (self.height == 0) or (self.width == 0):
            return ""
        else:
            append_row = ""
            first = True
            for i in range(self.height):
                if first is False:
                    hash_row = '\n' + ("#" * self.width)
                    append_row = append_row + hash_row
                else:
                    hash_row = ("#" * self.width)
                    append_row = append_row + hash_row
                    first = False
        return append_row
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
