#!/usr/bin/python3

# Initial list should not be modified
# have to use map
# Returns a new list:
# Same length as my_list
# Each value should be multiplied by number

def multiply_list_map(my_list=[], number=0):
    new_list = list(map(lambda x: x * number, my_list))
    return new_list
