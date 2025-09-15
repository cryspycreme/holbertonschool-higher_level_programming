#!/usr/bin/python3

"""
This function creates a class Square
"""


class Square:
    """
    Prints and positions a square of size and position
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        for new_line in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print("")


# x = no spaces before #
# y = no new lines before the square