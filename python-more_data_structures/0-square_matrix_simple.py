#!/usr/bin/python3

# Write a function that computes the square value of all integers of a matrix.
# should return a new matrix
# Each value in matrix should be the square of the value of the input
# initial matrix should not be modified

# OUTPUT
# [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 1. use lambda to create function to square each integer in matrix
# 2. map() to apply function to each int
# 3. list comprehension loop to loop through each row

def square_matrix_simple(matrix=[]):
    square = list(map(lambda x: [i**2 for i in x], matrix))
    return square
