#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if (length == 0):
        first_ch = "None"
    else:
        first_ch = sentence[:1]
    tuple = (length, first_ch)
    return tuple
