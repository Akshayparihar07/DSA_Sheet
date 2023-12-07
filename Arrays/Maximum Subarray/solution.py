class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables for tracking current sum and maximum sum
        current_sum, max_sum = 0, float('-inf')

        # Iterate through the array
        for i in range(len(nums)):
            # Add the current element to the current sum
            current_sum += nums[i]

            # Update the maximum sum if the current sum is greater
            if current_sum > max_sum:
                max_sum = current_sum

            # Reset the current sum to 0 if it becomes negative
            if current_sum < 0: 
                current_sum = 0

        # Return the maximum sum
        return max_sum
