class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Get the length of the cost list
        n = len(cost)

        # Initialize variables to store the minimum cost to reach each step
        first = cost[0]  # Minimum cost to reach the first step
        second = cost[1]  # Minimum cost to reach the second step

        # Iterate through the cost list starting from the third step
        for i in range(2, n):
            # Calculate the current minimum cost to reach the current step
            current = cost[i] + min(first, second)

            # Update variables for the next iteration
            first = second  # Update the minimum cost for the previous step
            second = current  # Update the minimum cost for the current step

        # Return the minimum cost to reach the top of the stairs
        return min(first, second)
