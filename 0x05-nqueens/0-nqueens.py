#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""


import sys


def is_safe(board, row, col, n):
    """
    Check if pieces are safe not attacking
    """
    # Check the column on top
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """
    Define how output will be printed
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def solve_nqueens(n):
    """
    Determines number of queens
    """
    if n < 4:
        print("N must be at least 4")
        return

    def solve(board, row):
        if row == n:
            print_solution(board)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    solve(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
