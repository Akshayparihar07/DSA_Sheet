def solve(text1, text2, i, j, memo):
    # Base case: If either string has reached the beginning, return 0
    if i < 0 or j < 0:
        return 0

    # Check if the result for the current state is already memoized
    if memo[i][j] != -1:
        return memo[i][j]

    match = 0
    # Check if the characters at the current positions match
    if text1[i] == text2[j]:
        # If there is a match, add 1 to the result and move to the previous characters
        match = solve(text1, text2, i-1, j-1, memo) + 1

    # If there is no match, explore two possibilities: moving one character back in either text
    not_match1 = solve(text1, text2, i, j-1, memo)  # Move back in text2
    not_match2 = solve(text1, text2, i-1, j, memo)  # Move back in text1

    # Update memo table with the maximum result among the three possibilities
    memo[i][j] = max(match, not_match1, not_match2)

    # Return the result for the current state
    return memo[i][j]

# Initialize memoization table with -1 values
memo = [[-1]*len(text2) for _ in range(len(text1))]

# Start the recursive function with the last indices of both texts
result = solve(text1, text2, len(text1)-1, len(text2)-1, memo)

# Return the final result
return result
