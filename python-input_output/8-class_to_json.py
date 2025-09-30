#!/usr/bin/python3

"""
Class to JSON Module
"""


# import json


def class_to_json(obj):
    """
    Function returns dictionary description for JSON object
    """
    dict = obj.__dict__
    return dict
    # return json.dumps(dict)
