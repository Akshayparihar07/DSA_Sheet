def solve_n_queens(n):
    # Initialize sets to keep track of occupied columns and diagonals
    occupied_columns = set()
    positive_diagonals = set()
    negative_diagonals = set()

    # Initialize result list to store valid configurations
    result = []

    # Initialize chessboard with empty cells
    chessboard = [["."]*n for _ in range(n)]

    def backtrack(row):
        # Base case: if all rows are filled, add current configuration to result
        if row == n:
            current_configuration = ["".join(row) for row in chessboard]
            result.append(current_configuration)
            return

        # Explore each column in the current row
        for col in range(n):
            # Check if the current position is safe
            if col in occupied_columns or row-col in negative_diagonals or row+col in positive_diagonals:
                continue

            # Mark the current position as occupied
            occupied_columns.add(col)
            positive_diagonals.add(row+col)
            negative_diagonals.add(row-col)
            chessboard[row][col] = "Q"

            # Recursively move to the next row
            backtrack(row+1)

            # Backtrack: undo the changes to explore other possibilities
            occupied_columns.remove(col)
            positive_diagonals.remove(row+col)
            negative_diagonals.remove(row-col)
            chessboard[row][col] = "."

    # Start the backtracking from the first row
    backtrack(0)

    return result
