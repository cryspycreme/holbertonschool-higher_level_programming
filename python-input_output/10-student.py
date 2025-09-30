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

    def to_json(self, attrs=None):
        """
        Function returns dict rep of object
        """
        class_dict = self.__dict__
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            result = {x: class_dict[x] for x in attrs if x in class_dict}
        else:
            result = class_dict
        
        sorted_result = dict(sorted(result.items(), key=lambda item: str(item[1])))
        return sorted_result