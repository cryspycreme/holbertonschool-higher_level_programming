#!/usr/bin/python3

"""
is_instance module
"""


def is_kind_of_class(obj, a_class):
    """
    Function returns whether an object is an instance of Class
    """
    return True if isinstance(obj, a_class) is True else False
