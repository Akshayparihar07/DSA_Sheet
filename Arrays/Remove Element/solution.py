class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer i to keep track of the position for non-val elements.
        i = 0

        # Iterate through the array using pointer j.
        for j in range(len(nums)):
            # If the current element is not equal to val, update the array at position i and move the pointer i.
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        # The final value of i represents the length of the new array without val.
        return i
