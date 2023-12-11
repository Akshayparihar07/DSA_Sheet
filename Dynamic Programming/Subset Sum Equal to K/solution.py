def subset_sum_exists(i, k, arr, dp):
    # Base case: if the target sum k is 0, an empty subset is a valid solution
    if k == 0:
        return True

    # Base case: if we have reached the first element in the array
    if i == 0:
        # Check if the current element equals the target sum
        return k - arr[i] == 0

    # If the result for the current state is already computed, return it
    if dp[i][k] is not False:
        return dp[i][k]

    # Recursively check two possibilities: 
    # 1. Exclude the current element and check if subset_sum exists
    not_take = subset_sum_exists(i - 1, k, arr, dp)

    # 2. Include the current element if it doesn't exceed the target sum
    take = False
    if k >= arr[i]:
        take = subset_sum_exists(i - 1, k - arr[i], arr, dp)

    # Update the result for the current state in the memoization table
    dp[i][k] = take or not_take

    return dp[i][k]

def main():
    # Input the size of the array
    n = int(input())
    
    # Input the array elements
    arr = list(map(int, input().split()))
    
    # Input the target sum to check for subset existence
    k = int(input())
    
    # Initialize a memoization table with False values
    dp = [[False] * (k + 1) for _ in range(n)] 
    
    # Call the recursive function and print the result
    return subset_sum_exists(n-1, k, arr, dp)

# Call the main function and print the result
print(main())
