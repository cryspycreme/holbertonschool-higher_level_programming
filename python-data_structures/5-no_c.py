#!/usr/bin/python3

def no_c(my_string):
    remove = "c", "C"
    screened_list = [x for x in my_string if x not in remove]
    screened_string = ''.join(screened_list)
    return screened_string
