class Solution:
    def adder(self, row, col, path_so_far, arr, n, vis, ans):
        # Check if the current position is within bounds
        if 0 <= row < n and 0 <= col < n:
            # Check if there is a wall (1) at the current position and it has not been visited
            if arr[row][col] == 1 and vis[row][col] == 0:
                # Mark the current position as visited
                vis[row][col] = 1

                # Check if the current position is the destination
                if row == col == n - 1:
                    ans.append(path_so_far)

                # Explore in all four directions: Down, Left, Up, Right
                self.adder(row + 1, col, path_so_far + "D", arr, n, vis, ans)  # Down
                self.adder(row, col - 1, path_so_far + "L", arr, n, vis, ans)  # Left
                self.adder(row - 1, col, path_so_far + "U", arr, n, vis, ans)  # Up
                self.adder(row, col + 1, path_so_far + "R", arr, n, vis, ans)  # Right

                # Backtrack by marking the current position as unvisited
                vis[row][col] = 0

    def findPath(self, m, n):
        # Start with an empty path and initialize the visited matrix
        start_path = ""
        visited = [[0] * n for _ in range(n)]

        # List to store all possible paths
        all_paths = []

        # Start the recursive exploration from the top-left corner
        self.adder(0, 0, start_path, m, n, visited, all_paths)

        return all_paths
