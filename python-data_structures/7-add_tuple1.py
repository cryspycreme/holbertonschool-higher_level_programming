#!/usr/bin/python3

#Adds (0, 0) → so even empty/short tuples get padded.
#Uses [:2] → so longer tuples are trimmed.

def normalise(tuple):
    return (tuple + (0, 0))[:2]

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = normalise(tuple_a)
    tuple_b = normalise(tuple_b)
    return tuple(map(sum, zip(tuple_a, tuple_b)))