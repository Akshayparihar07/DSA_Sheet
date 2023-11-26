from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of elements
        # Key: element, Value: index
        index_dict = {}

        # Iterate through the list to populate the dictionary
        for index, num in enumerate(nums):
            index_dict[num] = index

        # Iterate through the list again to find the pair
        for i, num in enumerate(nums):
            # Calculate the complement needed to achieve the target
            complement = target - num
            
            # Check if the complement is in the dictionary and the index is different
            if complement in index_dict and index_dict[complement] != i:
                # Return the indices of the two numbers that add up to the target
                return [index_dict[complement], i]
