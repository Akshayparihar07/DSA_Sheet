class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-1]*n

        # if I rob 0th house then I am defeitely not gonna rob 1st house because it's adjacent. 
        # Hence, I wanna make sure that the 0th house will give me maximum loot. so, I will keep nums[0]
        dp[0] = nums[0]


        for i in range(n):
            # for each house the robber will have two choices
                
            # 1. rob it and add the loot in the bag 
            rob = nums[i] + (dp[i-2] if i-2 >= 0 else 0)

            # 2. dont rob it and add nothing in the bag 
            dont_rob = dp[i-1] + 0

            # keep maximum loot in both the conditions
            dp[i] = max(rob, dont_rob)

        return dp[n-1]
