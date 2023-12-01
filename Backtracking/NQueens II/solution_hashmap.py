def n_queens_count(n):
    """
    Count the number of distinct solutions for placing n queens on an n x n chessboard
    without any two queens threatening each other.
    """
    # Sets to track occupied columns, positive diagonals, and negative diagonals
    occupied_columns = set()
    occupied_pos_diag = set()
    occupied_neg_diag = set()

    # Variable to store the total number of solutions
    total_solutions = 0

    def backtrack(row):
        """
        Backtracking function to explore all possible queen placements on the chessboard.
        """
        nonlocal total_solutions

        # If all queens are placed successfully, increment the solution count
        if row == n:
            total_solutions += 1
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            # Check if the current column, positive diagonal, and negative diagonal are available
            if col in occupied_columns or (row - col) in occupied_neg_diag or (row + col) in occupied_pos_diag:
                continue

            # Place the queen and update the occupied sets
            occupied_columns.add(col)
            occupied_pos_diag.add(row + col)
            occupied_neg_diag.add(row - col)

            # Recursively move to the next row
            backtrack(row + 1)

            # Remove the queen and backtrack to explore other possibilities
            occupied_columns.remove(col)
            occupied_pos_diag.remove(row + col)
            occupied_neg_diag.remove(row - col)

    # Start the backtracking process from the first row
    backtrack(0)

    return total_solutions
