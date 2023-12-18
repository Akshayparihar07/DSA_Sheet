n = len(coins)

# Initialize an array to store minimum number of coins needed for each amount
dp = [1e9]*(amount+1)

# Base case: 0 coins needed for amount 0
dp[0] = 0

# Iterate over each amount from 1 to the target amount
for i in range(1, amount + 1):
    # Iterate over each coin denomination
    for j in range(n):
        # Check if the current coin can be used to make change for the current amount
        if i >= coins[j] and dp[i-coins[j]] != 1e9:
            # Update the minimum number of coins needed for the current amount
            dp[i] = min(dp[i], 1 + dp[i-coins[j]])

# Return the minimum number of coins needed for the target amount
# If it's still set to the initial value (1e9), there's no valid combination, so return -1
return dp[amount] if dp[amount] != 1e9 else -1
