#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x_matrix = matrix
    for n in range(len(matrix)):
        x_matrix[n] = list(map(lambda x: x**2, matrix[n]))
    return x_matrix
