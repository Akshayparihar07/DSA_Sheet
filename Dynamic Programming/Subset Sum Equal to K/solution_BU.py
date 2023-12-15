# Initialize a 2D array dp with dimensions (N+1) x (sum+1) to store intermediate results
dp = [[None]*(sum+1) for _ in range(N+1)]

# Initialize the base cases for dynamic programming
# For s in range(sum+1), set dp[0][s] to False
for s in range(sum+1):
    dp[0][s] = False

# For n in range(N+1), set dp[n][0] to True
for n in range(N+1):
    dp[n][0] = True

# Populate the dp array using dynamic programming
# Iterate over the elements in arr and the possible sums
for i in range(1, N+1):
    for j in range(1, sum+1):
        # Check if the current element in arr is greater than the current sum
        if arr[i-1] > j:
            # If it is, set the current dp value to the value from the previous row
            dp[i][j] = dp[i-1][j]
        else:
            # If it's not, set the current dp value to the logical OR of two possibilities
            # 1. Exclude the current element and use the value from the previous row
            # 2. Include the current element and use the value from the row above and arr[i-1] steps back in the current row
            dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

# Return the final result stored in dp[N][sum]
return dp[N][sum]
