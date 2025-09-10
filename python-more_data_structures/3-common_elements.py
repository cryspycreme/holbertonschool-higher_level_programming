#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = {string for string in set_1 if string in set_2}
    return common_set
