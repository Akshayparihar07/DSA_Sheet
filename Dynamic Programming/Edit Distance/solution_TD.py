class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
    
        def strMatch(word1, word2, i, j, dp):
            # BASE CASE: If we have reached the end of one of the words,
            # return the remaining length of the other word.
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            # If the result for the current subproblem is already calculated, return it.
            if dp[i][j] != -1:
                return dp[i][j]

            # If the current characters match, no additional operation is needed.
            if word1[i] == word2[j]:
                dp[i][j] = strMatch(word1, word2, i - 1, j - 1, dp)
                return dp[i][j]

            # If characters don't match, calculate the minimum distance by considering
            # insertion, deletion, and replacement operations.
            insert = strMatch(word1, word2, i, j - 1, dp) + 1
            delete = strMatch(word1, word2, i - 1, j, dp) + 1
            replace = strMatch(word1, word2, i - 1, j - 1, dp) + 1

            # Update the result for the current subproblem in the DP table.
            dp[i][j] = min(insert, delete, replace)

            # Return the calculated result for the current subproblem.
            return dp[i][j]

        # Get the lengths of the input words.
        n = len(word1)
        m = len(word2)

        # Initialize a memoization table with -1 to store intermediate results.
        dp = [[-1] * m for _ in range(n)]

        # Start the recursive calculation from the end of both words.
        return strMatch(word1, word2, n - 1, m - 1, dp)
