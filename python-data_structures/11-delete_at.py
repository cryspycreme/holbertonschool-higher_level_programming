#!/usr/bin/python3

# If idx is negative or out of range, nothing change (returns the same list)
# You are not allowed to use pop()

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        del my_list[idx]
    return my_list
