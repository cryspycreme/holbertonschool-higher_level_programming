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
            i += 1
            # Skip *all* spaces after special char
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        else:
            print("{}".format(text[i]), end="")
        i += 1
