#!/usr/bin/python3

"""
Integer Validator Module
"""


class BaseGeometry:
    """
    Raise error that area is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
    """
    Function to validate integers
    """
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        if isinstance(name, type(value)):
            return


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
