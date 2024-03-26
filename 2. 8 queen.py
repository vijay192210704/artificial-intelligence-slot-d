def is_safe(board, row, col):
    """
    Check if placing a queen at position (row, col) is safe.
    """
    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_queens(board, col):
    """
    Recursive function to solve the 8-Queens problem.
    """
    # Base case: If all queens are placed
    if col >= len(board):
        return True

    # Try placing a queen in each row of the current column
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_queens(board, col + 1):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no queen can be placed in this column, return False
    return False


def print_solution(board):
    """
    Print the solution (board configuration) for the 8-Queens problem.
    """
    for row in board:
        print(" ".join(map(str, row)))


def solve_8_queens():
    """
    Solve the 8-Queens problem and print the solution.
    """
    board = [[0] * 8 for _ in range(8)]

    if solve_queens(board, 0):
        print("Solution:")
        print_solution(board)
    else:
        print("No solution found.")


# Example usage
solve_8_queens()
