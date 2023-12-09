class Solution:
    def isSubsetSum(self, N, arr, sum):
        def solve(i, sumi):
            # If the current subset sum equals the target sum
            if sumi == sum:
                return True
                
            # If we have processed all elements in the array
            if i >= N:
                return False

            # Try including the current element in the subset
            for j in range(i, N):
                if solve(j + 1, sumi + arr[j]):
                    return True

        # Start the recursive function with initial values
        if solve(0, 0):
            return True

        # If no subset with the target sum is found
        return False
