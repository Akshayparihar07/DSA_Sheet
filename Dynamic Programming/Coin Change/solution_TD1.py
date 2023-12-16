n = len(coins)

# Define a recursive function to find the minimum number of coins needed to make a given amount.
# i represents the index of the current coin, and dp is a memoization table to store intermediate results.
def minCoins(coins, amount, i, dp):
    # Base case: If we are considering the first coin (i=0),
    # check if the amount is divisible evenly by the coin. If so, return the quotient.
    if i == 0:
        if amount % coins[i] == 0:
            return amount // coins[i]

        # If not divisible, return a large value indicating that this combination is not valid.
        return 1e9

    # If the result for the current combination is already computed, return it.
    if dp[i][amount] != -1:
        return dp[i][amount]

    # Recursive cases:
    # 1. Do not take the current coin (move to the previous coin).
    not_take = 0 + minCoins(coins, amount, i-1, dp)

    # 2. Take the current coin if the amount is greater than or equal to the coin's value.
    take = 1e9
    if amount >= coins[i]:
        take = 1 + minCoins(coins, amount-coins[i], i, dp)

    # Update the memoization table with the minimum of the two choices.
    dp[i][amount] = min(take, not_take)

    # Return the minimum number of coins needed for the current combination.
    return dp[i][amount]

# Initialize a memoization table with -1 values.
dp = [[-1]* (amount+1) for _ in range(n+1)]

# Start with the last coin in the list (index n-1).
i = n-1

# Call the recursive function to find the minimum number of coins needed.
ans = minCoins(coins, amount, i, dp)

# If a valid combination is found, return the result; otherwise, return -1.
return ans if ans != 1e9 else  -1 
