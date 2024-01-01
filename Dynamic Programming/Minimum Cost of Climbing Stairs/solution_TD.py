class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Calculate the minimum cost of climbing stairs using dynamic programming.

        # Get the length of the cost array.
        n = len(cost)

        # Recursive function to calculate the minimum cost of climbing stairs.
        def climb(cost, n, dp):
            # Base case: If we are below the first step, the cost is zero.
            if n < 0: 
                return 0
            # Base cases: If we are on the first or second step, return the cost of that step.
            if n == 0:
                return cost[n]
            if n == 1:
                return cost[n]

            # If the minimum cost for the current step is already calculated, return it.
            if dp[n] != -1:
                return dp[n]

            # Calculate the minimum cost for the current step by considering two options:
            # 1. Climbing from the previous step.
            # 2. Climbing from two steps back.
            dp[n] = cost[n] + min(climb(cost, n-1, dp), climb(cost, n-2, dp))

            # Return the calculated minimum cost for the current step.
            return dp[n]

        # Initialize an array to store the minimum cost for each step, initially set to -1.
        dp = [-1]*n

        # Return the minimum cost of climbing stairs by considering starting from the last or second-to-last step.
        return min(climb(cost, len(cost)-1, dp), climb(cost, len(cost)-2, dp))
