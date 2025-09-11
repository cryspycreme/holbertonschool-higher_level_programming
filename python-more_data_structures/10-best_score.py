#!/usr/bin/python3

# Write a function that returns a key with the biggest integer value.

# You can assume that all values are only integers
# If no score found, return None
# You can assume all students have a different score

# sort dict by highest value
# return the key associated with the highest value
# if no score found, return None

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # sort dictionary by value, in ascending order
    top_score = max(a_dictionary.values())
    for name, score in a_dictionary.items():
        if score == top_score:
            champion = name
    return champion
