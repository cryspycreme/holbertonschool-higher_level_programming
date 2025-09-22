#!/usr/bin/python3

"""
Only subclass of module
"""


def inherits_from(obj, a_class):
    """
    Return True only if the object is an instance of a subclass, not the
    class itself.
    """
    return True if issubclass(type(obj), a_class) and (type(obj) is not
                                                       a_class) else False
