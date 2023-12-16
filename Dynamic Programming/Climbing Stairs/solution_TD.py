def climb(n, memo={}):
    # Base case: If the stair count is 0 or 1, there is only 1 way to climb.
    if n <= 1:
        return 1

    # Initialize the count of ways to climb the stairs.
    ways = 0
    
    # Check if the number of ways to climb 'n' stairs is already stored in the memo dictionary.
    if n not in memo:
        # Recursively calculate the number of ways to climb 'n-1' and 'n-2' stairs.
        ways += climb(n-1) + climb(n-2)
        
        # Store the result in the memo dictionary to avoid redundant calculations.
        memo[n] = ways

    # Return the number of ways to climb 'n' stairs.
    return memo[n]
