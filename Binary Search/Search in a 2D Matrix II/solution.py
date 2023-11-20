class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Check if there is only one row in the matrix
        if len(matrix) == 1:
            # Perform binary search in the single row
            low, high = 0, len(matrix[0]) - 1
            arr = matrix[0]
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
        else:
            # Start from the bottom-left corner of the matrix
            row, col = len(matrix) - 1, 0
            
            # Traverse the matrix
            while row >= 0 and col < len(matrix[0]):
                # If the current element is equal to the target, return True
                if matrix[row][col] == target:
                    return True
                # If the current element is less than the target, move right in the same row
                if matrix[row][col] < target:
                    col += 1
                # If the current element is greater than the target, move up to the previous row
                else:
                    row -= 1
            
            # If the target is not found in the matrix, return False
            return False
