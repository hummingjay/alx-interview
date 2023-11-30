#!/usr/bin/python3
"""
Function that returns the perimeter of the
island deascribed as a grid
where 0 is water and 1 is land
"""


def island_perimeter(grid):
    """
    Method that takes in the grid to find
    the perimeter of the 'Island' and return the perimeter
    """
    perimeter = 0
    m = len(grid)

    for i in range(m):
        n = len(grid[i])
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if j < n - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
                if i < m - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
    return (perimeter)
