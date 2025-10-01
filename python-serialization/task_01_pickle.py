#!/usr/bin/env python3

"""
Pickling custom classes module
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Function initialises object
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Function prints out the objects attributes in desired format
        """
        cobj_dict = self.__dict__
        for key, value in cobj_dict.items():
            new_key = key.replace("_", " ")
            new_key = new_key.title()
            # key.replace("_", " ").title() <- you can stack methods like this
            print("{}: {}".format(new_key, value))

    def serialize(self, filename):
        """
        Function serializes object
        """
        with open(filename, "wb") as srlz:
            return pickle.dump(self, srlz)

    @classmethod
    def deserialize(cls, filename):
        """
        Function deserializes object
        """
        with open(filename, "rb") as dsrlz:
            try:
                return pickle.load(dsrlz)
            except EOFError:
                exit
