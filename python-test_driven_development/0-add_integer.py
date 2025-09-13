#!/usr/bin/python3

"""
This is a function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    Sum the values of a and b
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):         raise TypeError("b must be an integer")
    return int(a) + int(b)
