# Initialize a 2D array dp with dimensions (n+1) x (W+1) and fill it with -1
dp = [[-1]*(W+1) for _ in range(n+1)]

# Initialize the base case: If the weight (W) is 0, then the value is 0
for i in range(W+1):
    dp[0][i] = 0

# Initialize the base case: If there are no items (n), then the value is 0
for j in range(n+1):
    dp[j][0] = 0

# Fill in the DP table using bottom-up approach
for i in range(1, n+1):
    for j in range(1, W+1):
        # If the current item's weight is greater than the current capacity (j),
        # then the optimal value is the same as the value without including the current item
        if wt[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            # Otherwise, choose the maximum between not including the current item
            # and including the current item in the knapsack
            dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i-1][j-wt[i-1]])

# The final result is stored in dp[n][W], which represents the maximum value
return dp[n][W]
