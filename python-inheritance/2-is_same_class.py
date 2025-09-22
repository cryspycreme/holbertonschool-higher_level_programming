#!/usr/bin/python3

"""
same_class module
"""


def is_same_class(obj, a_class):
    """
    Function checks for exactly the same class
    """
    return True if type(obj) is a_class else False
