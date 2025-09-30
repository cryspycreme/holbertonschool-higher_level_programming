#!/usr/bin/python3

"""
Student to JSON module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instantiate student object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Function returns dict rep of object
        """
        return self.__dict__
