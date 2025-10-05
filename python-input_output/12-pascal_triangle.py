#!/usr/bin/python3

"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    Function returns a list of lists of ints
    """
    res = [[1]]

    for i in range(n - 1): #-1 because we already made one row is res
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res


# if n <= 0, return an empty list
# n is always an int
# each subsequent row is double the sum of the prev row

# in pascal's triangle, each number is the sum of the two numbers directly above it as shown
# assume there is a 0 at the beginning and end of each row, and use pointers to shift and build the row

# [1]  1, row 0
# [1,1]. 2, row 1
# [1,2,1]. 4, row 2
# [1,3,3,1]. 8, row 3
# [1,4,6,4,1]. 16, row 4

