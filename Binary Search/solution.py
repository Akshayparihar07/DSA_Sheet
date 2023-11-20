class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def elem_search(matrix_row, target, m):
            low = 0
            high = m-1
            while low <= high:
                mid = (low+high) // 2

                if matrix_row[mid] == target:
                    return True
                if target > matrix_row[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return False

        n = len(matrix)
        for r in range(n):
            m = len(matrix[r])
            if matrix[r][0] <= target <= matrix[r][m - 1]:
                if elem_search(matrix[r], target, m):
                    return True
        return False
