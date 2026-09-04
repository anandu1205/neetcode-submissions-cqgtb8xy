from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2

                if matrix[r][mid] == target:
                    return True

                if matrix[r][mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

        return False