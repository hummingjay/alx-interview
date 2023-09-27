#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    function that returns a pascal triangle in form of lists
    """
    triangle = []
    if (n <= 0):
        return []

    for i in range(n):
        row = []
        c = 1
        for j in range(i + 1):
            row.append(c)

            c = c * (i - j) // (j + 1)
        triangle.append(row)
    return triangle
