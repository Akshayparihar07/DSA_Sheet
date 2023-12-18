#   NOTE : THIS SOLUTION WILL THROW SEGMENTATION FAULT ON GFG SO GO FOR BOTTOM-UP(TABULATION) SOLUTION👨🏻‍💻

class Solution:
    def rob(self, nums: List[int]) -> int:
      
        n = len(nums)

        def Rob_DontRob(nums, n, dp):
            
            # if n-2 goes beyond len(nums) then return 0
            if n < 0:
                return 0
                
            # Note: if I rob 0th house then I am defeitely not gonna rob 1st house because it's adjacent. 
            # Hence, I wanna make sure that the 0th house will give me maximum loot. so, I will return nums[0]
            if n == 0:
                return nums[0]
                
            # dp check
            if (dp[n] == -1):
                # for each house the robber will have two choices
                
                # 1. rob it and add the loot in the bag 
                rob = nums[n] + Rob_DontRob(nums, n-2, dp)
                
                # 2. dont rob it and add nothing in the bag 
                dont_rob = Rob_DontRob(nums, n-1, dp) + 0
                
                
                # return maximum loot in both the conditions
                dp[n] = max(rob, dont_rob)
                
            return dp[n]
            
        dp = [-1]*n
        return Rob_DontRob(nums, n-1, dp)
