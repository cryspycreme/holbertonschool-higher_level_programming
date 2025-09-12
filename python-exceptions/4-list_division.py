#!/usr/bin/python3

# 1. Return a new list with all divisions
# ALG: use list comprehension to create a new list, lambda to create the
# temp function, map() to apply the function across the list.

def list_division(my_list_1, my_list_2, list_length):
    quotient = []
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        finally:
            quotient.append(result)
    return quotient
