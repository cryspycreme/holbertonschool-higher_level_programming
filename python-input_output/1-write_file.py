#!/usr/bin/python3

"""
Write module
"""


def write_file(filename="", text=""):
    """
    Function writes string to text file and returns no. bytes written
    """
    with open(filename, "w") as file:
        return file.write(text)
