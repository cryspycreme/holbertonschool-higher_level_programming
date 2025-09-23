#!/usr/bin/python3


"""
Square 2 Module
"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """
    subclass Square
    """
    def __init__(self, size):
        """
        Initialise with width and height from size
        """
        # validate once with the ngith name
        super().integer_validator("size", size)
        # if we want to access the Rectangle attributes and set to size
        self._Rectangle__width = size
        self._Rectangle__height = size
        # super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        returns formatted string
        """
        # return ("{} {}/{}".format(self.__class__.__name__, self.
        # _Rectangle__width, self._Rectangle__height))
        return super().__str__()
