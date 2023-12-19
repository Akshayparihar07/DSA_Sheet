class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of the input words
        n = len(word1)
        m = len(word2)
        
        # Initialize a 2D array to store subproblem solutions
        dp = [[-1] * (m+1) for _ in range(n+1)]

        # Base case: 0th row represents converting an empty string to word2
        for j in range(m+1):
            dp[0][j] = j

        # Base case: 0th column represents converting word1 to an empty string
        for i in range(n+1):
            dp[i][0] = i

        # Fill in the DP table by considering all possible operations
        for i in range(1, n+1):
            for j in range(1, m+1):
                # If the characters at the current positions are the same
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Calculate the cost of different operations
                    insert = dp[i][j-1] + 1
                    delete = dp[i-1][j] + 1
                    replace = dp[i-1][j-1] + 1

                    # Choose the minimum cost among insert, delete, and replace
                    dp[i][j] = min(insert, delete, replace)

        # The final value in the DP table represents the minimum edit distance
        return dp[n][m]
