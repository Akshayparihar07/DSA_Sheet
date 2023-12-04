class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num1 = set(nums)
        return len(nums) != len(num1)
