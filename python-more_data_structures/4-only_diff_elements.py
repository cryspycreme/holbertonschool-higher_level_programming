#!/usr/bin/python3

# Write a function that returns a set of all elements present in only one set.

def only_diff_elements(set_1, set_2):
    set_3 = set_1.union(set_2)
    new_set = {string for string in set_3 if string in (set_1 ^ set_2)}
    return new_set
