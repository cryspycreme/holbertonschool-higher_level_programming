#!/usr/bin/python3

"""
Basic Serialization module
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function serializes a Python dict to JSON file
    """
    with open(filename, "w", encoding="utf-8") as srl:
        return json.dump(data, srl)


def load_and_deserialize(filename):
    """
    Function deserializes a JSON File to Python dict
    """
    with open(filename, encoding="utf-8") as dsrl:
        return json.load(dsrl)
