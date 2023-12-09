n = len(nums)

# Define the recursive function to generate all subsets
def generateSubsets(i, ans, subset):
    # Base case: reached the end of the array
    if i == n:
        ans.append(subset[:])
        return 

    # Recursive call with taking the current element
    subset.append(nums[i])
    generateSubsets(i+1, ans, subset)

    # Recursive call without taking the current element (backtrack)
    subset.pop()
    generateSubsets(i+1, ans, subset)

    # OR
            '''
            # Not Take
            genrateSubsets(i + 1, ans, subset)

            # Take
            subset.append(nums[i])
            genrateSubsets(i + 1, ans, subset)

            # Backtrack
            subset.pop()
            '''

# Initialize variables and start recursion
ans = []
subset = []
i = 0
generateSubsets(i, ans, subset)

# Return the generated subsets
return ans
