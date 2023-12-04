class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer 'i' to track the unique elements
        i = 0

        # Iterate through the array with a pointer 'j'
        for j in range(len(nums)):
            # Check if the current element is different from the element at 'i'
            if nums[j] != nums[i]:
                # Move 'i' to the next position and update the element at that position
                i += 1
                nums[i] = nums[j]

        # Return the length of the unique elements (index + 1)
        return i + 1
