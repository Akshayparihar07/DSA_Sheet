def solve(text1, text2, i, j, memo):
    # Base case: If either of the indices is less than 0, no more characters to compare.
    if i < 0 or j < 0:
        return 0

    # Check if the result for the current indices is already computed and stored in memo.
    if memo[i][j] != -1:
        return memo[i][j]

    match = 0
    # Check if the current characters in both texts match.
    if text1[i] == text2[j]:
        # If there's a match, recursively call solve for the previous characters in both texts.
        match = solve(text1, text2, i-1, j-1, memo) + 1

    # Recursively call solve for the case where the current character in text2 is skipped.
    match1 = solve(text1, text2, i, j-1, memo)
    # Recursively call solve for the case where the current character in text1 is skipped.
    match2 = solve(text1, text2, i-1, j, memo)

    # Store the maximum of the three cases in memo for future reference.
    memo[i][j] = max(match, match1, match2)

    # Return the maximum match count for the current indices.
    return memo[i][j]

# Initialize memoization table with -1 for each combination of indices.
memo = [[-1] * len(text2) for _ in range(len(text1))]

# Start solving the problem from the last characters of both texts.
result = solve(text1, text2, len(text1)-1, len(text2)-1, memo)

# Return the final result.
return result
