class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result list to store permutations
        permutations = []

        # Helper function for backtracking
        def backtrack(start_index):
            # If we have reached the end of the array, add the current permutation to the result
            if start_index == len(nums):
                permutations.append(nums.copy())
                return

            # Explore all possible swaps starting from the current index
            for i in range(start_index, len(nums)):
                # Swap elements at the current index and i
                nums[i], nums[start_index] = nums[start_index], nums[i]

                # Recursively generate permutations for the remaining elements
                backtrack(start_index + 1)

                # Backtrack: Undo the swap to explore other possibilities
                nums[start_index], nums[i] = nums[i], nums[start_index]

        # Start the backtracking process from the beginning of the array
        backtrack(0)

        return permutations
