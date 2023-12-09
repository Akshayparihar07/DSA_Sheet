class Solution:
    def isSubsetSum(self, N, arr, Sum):
        def solve(i, current_sum):
            # If the current subset sum equals the target sum
            if current_sum == Sum:
                return True
                
            # If we have processed all elements in the array
            if i >= N:
                return False

            # Try including the current element in the subset
            for j in range(i, N):
                if solve(j + 1, current_sum + arr[j]):
                    return True

        # Start the recursive function with initial values
        if solve(0, 0):
            return True

        # If no subset with the target sum is found
        return False
