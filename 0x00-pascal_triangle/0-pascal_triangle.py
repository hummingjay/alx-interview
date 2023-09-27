#!/usr/bin/python3
def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        c = 1
        for j in range(i + 1):
            row.append(c)

            c = c * (i - j) // (j + 1)
        triangle.append(row)
    return triangle
