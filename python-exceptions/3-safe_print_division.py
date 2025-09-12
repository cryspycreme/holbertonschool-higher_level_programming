#!/usr/bin/python3

# Write a function that divides 2 integers and prints the result.
# The result of the division should print on the finally: section preceded
# by Inside result:
# Returns the value of the division, otherwise: None
# You have to use "{}".format() to print the result

def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = "None"
        return result
    finally:
        print("Inside Result: {}".format(result))
