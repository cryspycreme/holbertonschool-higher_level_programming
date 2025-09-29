#!/usr/bin/python3

"""
Save object to JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an object to a JSON text file
    """
    with open("my_obj.json", "w") as filename:
        return json.dump(my_obj, filename)
