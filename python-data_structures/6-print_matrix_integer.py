#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        print("{:d}".format(matrix[idx]))
        matrix[idx] = []
