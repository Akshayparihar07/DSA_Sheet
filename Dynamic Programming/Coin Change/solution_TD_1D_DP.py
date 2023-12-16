n = len(coins)

def minCoins(coins, amount, dp):
    # Base case: If the amount is already 0, no coins are needed.
    if amount == 0:
        return 0
    
    # Base case: If the amount is negative, it is not a valid solution.
    if amount < 0:
        return 1e9
    
    # If the result for the current amount is already computed, return it.
    if dp[amount] != -1:
        return dp[amount]

    # Initialize the minimum value for the current amount.
    minimum = 1e9
    
    # Iterate through each coin to find the minimum number of coins needed.
    for i in range(n):
        minimum = min(1 + minCoins(coins, amount - coins[i], dp), minimum)

    # Save the computed result to avoid redundant calculations.
    dp[amount] = minimum

    return dp[amount]

# Initialize the dynamic programming array with -1.
dp = [-1] * (amount + 1)

# Calculate the minimum number of coins needed for the given amount.
ans = minCoins(coins, amount, dp)

# Return the result if a valid solution is found, otherwise, return -1.
return ans if ans != 1e9 else -1
