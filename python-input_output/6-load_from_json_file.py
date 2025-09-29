#!/usr/bin/python3

"""
Create object from JSON module
"""


import json


def load_from_json_file(filename):
    """
    Function creates an object from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
