# Initialize a memoization table dp with default value -1
dp = [[-1]*(W+1) for _ in range(n+1)]

# Define the knapsack function using recursion and memoization
def knapSack(W, wt, val, n):
    # Base Case: If the capacity W is 0 or no items are left
    if W == 0 or n == 0:
        return 0
        
    # If the result for the current state is already memoized, return it
    if dp[n][W] != -1:
        return dp[n][W]
        
    # If the weight of the current item is more than the remaining capacity W,
    # exclude the item from the knapsack
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)
        
    else:
        # Choose the maximum value between excluding the current item and
        # including the current item in the knapsack
        dp[n][W] = max(knapSack(W, wt, val, n-1), (val[n-1] + knapSack(W-wt[n-1], wt, val, n-1)))
        
    # Return the maximum value for the current state and update the memoization table
    return dp[n][W]

# Call the knapsack function with the given parameters
return knapSack(W, wt, val, n)
