class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Sort the given array in ascending order
        nums.sort()

        # Initialize a pointer variable for comparison
        j = 0
        
        # Iterate through the array starting from index 1
        for i in range(1, len(nums)):
            # Check if the current element is equal to the previous element
            if nums[i] == nums[j]:
                # If duplicates are found, return True
                return True
            
            # Move the pointer to the next element
            j += 1
        
        # If no duplicates are found, return False
        return False
