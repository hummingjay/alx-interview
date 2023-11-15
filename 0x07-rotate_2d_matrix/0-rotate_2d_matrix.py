#!/usr/bin/python3
"""
Method that rotates a 2d matrix by 90 degrees
matrix - input
"""


def rotate_2d_matrix(matrix):
    """
    Function that takes in the matrix to be rotated
    finds the value of n in nxn matrix then rotates
    by 90 degrees
    """


    n = len(matrix)

    # transpose matrix aka switch row and column
    for x in range(n):
        for y in range(x + 1, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    # reverse each row to finish clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]
