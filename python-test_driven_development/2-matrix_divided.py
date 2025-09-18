#!/usr/bin/python3

# matrix rows must be the same size - TypeError
# matrix must contain int or floats - TypeError
# div must be an int or float - TypeError
# div != 0 - ZeroDivision Error
# output should be {:2d}

"""
This is a function that divides each row of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divide each value in the matrix
    """

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrix_1 = []
    for row in matrix:
        row_length = len(matrix[0])
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list "
                                "of lists) of integers/floats")
            divided = round((num / div), 2)
            new_row.append(divided)
        matrix_1.append(new_row)
    return matrix_1
