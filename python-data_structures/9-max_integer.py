#!/usr/bin/python3

# return max integer in the list
# if list is empty, return None

def max_integer(my_list=[]):
    sort_list = list(sorted(my_list))
    if my_list == []:
        return None
    else:
        max_int = sort_list[-1]
    return max_int
