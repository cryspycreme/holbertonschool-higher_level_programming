#!/usr/bin/python3

"""
Append module
"""


def append_write(filename="", text=""):
    "Function appends a string at the end of the text file "
    "and returns no. bytes added"
    with open(filename, "a") as file:
        return file.write(text)
