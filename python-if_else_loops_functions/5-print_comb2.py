#!/usr/bin/python3

# 1. if first, dont print comma
# 2. if number < 10, print 0 in front of number
# 3. if last, print a new line

for c in range(0, 100):
    if c != 99:
        print("{num:02d}, ".format(num=c), end="")
    else:
        print("{num:02d}".format(num=c))
