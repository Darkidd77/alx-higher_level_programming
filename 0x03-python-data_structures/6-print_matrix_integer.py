#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for n in x:
            print("{:d}".format(n), end=" " if n != x[-1] else "")
        print()
