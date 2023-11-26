from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the final subsets
        result = []
        
        # Call the recursive helper function to generate subsets
        self._generate_subsets(nums, 0, [], result)
        
        # Return the final list of subsets
        return result

    def _generate_subsets(self, nums, index, current_subset, result):
        """
        Recursive helper function to generate subsets of the given list of numbers.

        Parameters:
        - nums: The input list of numbers
        - index: The current index in the iteration
        - current_subset: The current subset being generated
        - result: The list to store the final subsets
        """

        # Base case: if the current index is equal to the length of the input list,
        # then we have reached the end of the list, and the current subset is a valid subset.
        if index == len(nums):
            result.append(current_subset[:])  # Append a copy of the current subset to the result
            return

        # Include the current element at the index in the subset and recurse
        self._generate_subsets(nums, index + 1, current_subset + [nums[index]], result)

        # Exclude the current element at the index and recurse
        self._generate_subsets(nums, index + 1, current_subset, result)
