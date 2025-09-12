#!/usr/bin/python3

"""
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You are not allowed to use len()

function should print the result & return the number of items printed
"""


def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    print("")
    return count
