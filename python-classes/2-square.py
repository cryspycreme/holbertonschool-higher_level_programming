#!/usr/bin/python3

"""
This function creates a class Square with size attribute and error msg
"""


class Square:
    """
    Instantiates Square size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
