class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        prev2 = 0 # Placed at -1 hence assigned 0 initially
        prev1 = nums[0] # Placed at 0th index

        for i in range(1, n):
            take = prev2 + nums[i] # Take the Non Adjacent
            not_take = prev1 + 0   # Don't take the Adjacent
            
            # assign maximum to the current pointer
            current = max(take, not_take)

            # Move the Pointers 
            prev2 = prev1 
            prev1 = current


        return prev1
