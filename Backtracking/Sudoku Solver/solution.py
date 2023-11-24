n = 9

def isValid(row, col, ch):
    """
    Check if placing the character 'ch' at position (row, col) is valid in the Sudoku board.
    """
    row, col = int(row), int(col)

    # Check if 'ch' is not present in the same row or column
    for i in range(9):
        if board[i][col] == ch or board[row][i] == ch:
            return False

    # Check if 'ch' is not present in the 3x3 subgrid
    for i in range(3):
        for j in range(3):
            if board[3*(row//3) + i][3*(col//3) + j] == ch:
                return False

    return True

def solve(row, col):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    if row == n:
        # All rows are filled, solution found
        return True
    if col == n:
        # Move to the next row
        return solve(row + 1, 0)

    if board[row][col] == ".":
        # Try placing digits from 1 to 9
        for i in range(1, 10):
            if isValid(row, col, str(i)):
                board[row][col] = str(i)

                # Recursively solve for the next cell
                if solve(row, col + 1):
                    return True
                else:
                    # Backtrack if the current placement is not valid
                    board[row][col] = "."
        return False
    else:
        # Cell is already filled, move to the next column
        return solve(row, col + 1)

# Example Sudoku board represented as a list of lists
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Solve the Sudoku puzzle
solve(0, 0)

# Print the solved Sudoku board
for row in board:
    print(" ".join(row))
