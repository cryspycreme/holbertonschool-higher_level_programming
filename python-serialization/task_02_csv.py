#!/usr/bin/env python3

"""
CSV to JSON Module
"""


import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, encoding="utf-8") as csvfile:
            # creates a DictReader object
            reader = list(csv.DictReader(csvfile))
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(reader, jsonfile, indent=4)
        return True
    except Exception:
        return False
