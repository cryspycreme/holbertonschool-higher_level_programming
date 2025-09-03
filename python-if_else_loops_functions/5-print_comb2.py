#!/usr/bin/python3

for c in range(0, 100):
    if c != 99:
        print("{num:02d}, ".format(num=c), end="")
    else:
        print("{num:02d}".format(num=c))
