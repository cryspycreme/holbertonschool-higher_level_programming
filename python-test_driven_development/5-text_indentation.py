#!/usr/bin/python3

"""
Function prints a text with 2 newlines after special characters.
"""


def text_indentation(text):
    """
    Function to print new lines after special characters
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    spcl = ['.', '?', ':']
    i = 0
    while i < len(text):
        if text[i] in spcl:
            print("{}".format(text[i]), end="")
            print("\n")
        elif text[i] == " " and text[i - 1] in spcl:
            print("", end="")
        else:
            print("{}".format(text[i]), end="")
        i += 1
