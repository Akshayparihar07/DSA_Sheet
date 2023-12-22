def generate_subsequences(s):
    # Helper function for backtracking
    def backtrack(start, current):
        # Add the current combination to the result
        ans.append(''.join(current))
        
        # Explore all possible subsequences by iterating over the remaining characters in s
        for i in range(start, len(s)):
            # Include the current character in the subsequence
            current.append(s[i])
            
            # Recursively backtrack to explore all subsequences
            backtrack(i + 1, current)
            
            # Backtrack by removing the last character to explore other possibilities
            current.pop()

    # Initialize the result list to store all generated subsequences
    ans = []
    
    # Start backtracking from the beginning of the input string
    backtrack(0, [])
    
    # Return the final list of subsequences
    return ans
