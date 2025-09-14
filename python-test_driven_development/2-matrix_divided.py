#!/usr/bin/python3

# matrix rows must be the same size - TypeError
# matrix must contain int or floats - TypeError
# div must be an int or float - TypeError
# div != 0 - ZeroDivision Error
# output should be {:2d}

def matrix_divided(matrix, div):
    matrix_1 = []
    if type(div) is not int and type(div) is not float:
        raise TypeError("division by zero")
    for i in range(len(matrix)):
        if (len(matrix[0]) is not len(matrix[1])):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            num = matrix[i][j]
            if num is None or (type(num) is not int and type(num) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divided = round((matrix[i][j] / div), 2)
            matrix_1.append(divided)
    return matrix_1
