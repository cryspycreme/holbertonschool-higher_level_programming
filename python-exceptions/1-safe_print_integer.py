#!/usr/bin/python3

# if value is int return True
# if value is not int, return False

def safe_print_integer(value):
    try:
        if value is int:
            return True
    except TypeError:
        return False
