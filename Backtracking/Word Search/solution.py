class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        n, m = len(board), len(board[0])
        
        # Set to keep track of visited cells
        visited = set()

        # Define the depth-first search function
        def dfs(r, c, i, word):
            # Base case: If all characters in the word are found, return True
            if i == len(word):
                return True

            # Invalid or edge cases for recursion
            if (
                r < 0 or c < 0 or r >= n or c >= m
                or word[i] != board[r][c]
                or (r, c) in visited
            ):
                return False

            # Mark the current cell as visited
            visited.add((r, c))

            # Explore neighboring cells in all four directions
            result = (
                dfs(r + 1, c, i + 1, word)
                or dfs(r - 1, c, i + 1, word)
                or dfs(r, c + 1, i + 1, word)
                or dfs(r, c - 1, i + 1, word)
            )

            # Backtrack: Remove the current cell from the visited set
            visited.remove((r, c))

            return result

        # Iterate through all cells in the board
        for i in range(n):
            for j in range(m):
                # Start DFS from each cell with the first character of the word
                if dfs(i, j, 0, word):
                    return True

        # If no match is found, return False
        return False
