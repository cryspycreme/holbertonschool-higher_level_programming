#!/usr/bin/python3

# my_list is the initial list
# search is the element to replace in the list = 2
# replace is the new element = 89

# if num == 2, replace that instance with 89

def search_replace(my_list, search, replace):
    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return new_list
