#!/usr/bin/python3

"""
Convert to Python from JSON module
"""


import json


def from_json_string(my_str):
    """
    Function returns an object represented by JSON string
    """
    return json.loads(my_str)
