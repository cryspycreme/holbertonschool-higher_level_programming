#!/usr/bin/python3

roman_set = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman_list = list(reversed(roman_string))
    total = 0
    prev_value = 0

    for i in range(len(roman_list)):
        current_val = roman_set.get(roman_list[i])
        if current_val < prev_value:
            total = total - current_val
        else:
            total = total + current_val
        prev_value = current_val
    return total

# define I, V, X, L, C, D in a dict
# convert the string into an iterable/list so we can iterate over it?
# loop over the list and use get(key) to return the value of the key
# if I is before V, X then subtract -> if current val is < pre_value
# if I is after V, X then add

# I = 1
# II = 2
# III = 3
# IV = 4
# V = 5
# VI = 6
# VII = 7
# VIII = 8
# IX = 9
# X = 10
# XX = 20
# L = 50
# C = 100
# D = 500
