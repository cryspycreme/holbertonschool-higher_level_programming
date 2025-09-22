#!/usr/bin/python3

"""
Sort module
"""


class MyList(list):
    def print_sorted(self):
        """
        Function prints the list, but sorted (ascending sort)
        """
        x = sorted(self)
        print(x)
