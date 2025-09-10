#!/usr/bin/python3

# Write a function that adds all unique integers in a list

# 1. turn the list into a set - this removes the duplicates
# 2. sum the set
# 3. return the set

def uniq_add(my_list=[]):
    my_set = set(my_list)
    add = sum(my_set)
    return add
