def climb(n):
    # Base case: If the stair count is 0 or 1, there is only 1 way to climb.
    if n <= 1:
        return 1

    # Initialize a list to store the number of ways to climb each step.
    ways = [0] * (n + 1)

    # Base cases: There is 1 way to climb 0 and 1 stairs.
    ways[0], ways[1] = 1, 1

    # Calculate the number of ways to climb each step from bottom up.
    for i in range(2, n + 1):
        ways[i] = ways[i-1] + ways[i-2]

    # Return the number of ways to climb 'n' stairs.
    return ways[n]
