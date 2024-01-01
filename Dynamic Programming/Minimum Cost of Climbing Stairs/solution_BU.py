class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Get the number of steps in the staircase
        n = len(cost)
        
        # Initialize an array to store the minimum cost to reach each step
        dp = [-1] * n
        
        # Set the base cases for the first two steps
        dp[0] = cost[0]
        dp[1] = cost[1]

        # Iterate through the remaining steps starting from the third step
        for i in range(2, n):
            # Calculate the minimum cost to reach the current step
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        # Return the minimum cost to reach the top of the staircase
        return min(dp[n-1], dp[n-2])
