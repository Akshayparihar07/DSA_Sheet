def solve(nums, i, subset, ans):
    # Append the current subset to the result
    ans.append(subset[:])  

    # Explore all possible subsets by recursively adding elements
    for j in range(i, len(nums)):
        subset.append(nums[j])  
        solve(nums, j + 1, subset, ans)
        subset.pop()

# Main function to generate all subsets of a given list of numbers
def generateSubsets(nums):
    ans = []        # Resultant list to store all subsets
    subset = []     # Current subset being constructed
    i = 0           # Starting index for subset generation
    
    # Start the recursive subset generation process
    solve(nums, i, subset, ans)
    
    return ans      # Return the final list of subsets
