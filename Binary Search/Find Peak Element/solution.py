def findPeakElement(self, nums: List[int]) -> int:
        # Function to find a peak element in the given array nums
        # A peak element is an element that is greater than its neighbors.

        # Edge cases
        n = len(nums)
        if n == 1:
            return 0  # Single element is a peak
        if nums[n - 2] < nums[n - 1]:
            return n - 1  # Last element is a peak
        if nums[0] > nums[1]:
            return 0  # First element is a peak

        # Binary search to find the peak element
        low, high = 0, n - 1

        while low <= high:
            mid = low + (high - low) // 2
            left, right = mid - 1, mid + 1

            # Check if mid is a peak
            if nums[left] < nums[mid] > nums[right]:
                return mid

            # If the left neighbor is greater, search in the left half
            if nums[left] > nums[mid]:
                high = mid - 1
            # Otherwise, search in the right half
            else:
                low = mid + 1

        # No peak found (should not reach here for a valid input)
        return -1
