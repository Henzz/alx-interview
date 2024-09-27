#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_n_queens_util(board, col, n, solutions):
    if col >= n:
        solutions.append(board.copy())
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            solve_n_queens_util(board, col + 1, n, solutions)


def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(board, 0, n, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
