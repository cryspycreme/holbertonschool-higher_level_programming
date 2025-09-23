#!/usr/bin/python3

"""
Base Geometry Module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    subclass Rectangle
    """
    def __init__(self, width, height):
        """
        Method to instantiate Rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height))
