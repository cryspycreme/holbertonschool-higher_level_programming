#!/usr/bin/python3

"""
Read file module
"""

def read_file(filename=""):
    """
    Function reads file and prints to output
    """
    with open("my_file_0.txt", encoding="utf-8") as file:
        for text in file:
            print("{}".format(text.rstrip()))
