#!/usr/bin/python3

"""
Read file module
"""


def read_file(filename=""):
    """
    Function reads file and prints to output
    """
    with open(filename, encoding="utf-8") as file:
        for lines in file:
            print("{}".format(lines.rstrip()))
