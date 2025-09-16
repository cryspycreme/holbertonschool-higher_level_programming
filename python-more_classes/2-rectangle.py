#!/usr/bin/python3
#!/usr/bin/python3

"""
This is a function that creates an empty Class called Rectangle
"""


class Rectangle:
    """
    Initiate method to create new object/instance of class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
