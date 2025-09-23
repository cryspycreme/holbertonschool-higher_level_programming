#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
Square 1 Module
"""


class Square(Rectangle):
    """
    subclass Square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
