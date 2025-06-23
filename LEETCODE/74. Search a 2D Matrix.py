from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        top, bottom = 0, m - 1
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2

            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            if matrix[mid][0] < target:
                top = mid + 1
            else: #  matrix[r_mid][0] > target
                bottom = mid - 1

        if row == -1:
            return False

        left, right = 0, n-1
        while left  <= right:
            col = (left + right) // 2
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = col + 1
            else: # matrix[row][c_mid] > target
                right = col - 1

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# target = 13
s = Solution()
# print(s.searchMatrix(matrix, target))
print(s.searchMatrix(matrix, 3))    # ✅ True
print(s.searchMatrix(matrix, 13))   # ✅ False
print(s.searchMatrix(matrix, 60))   # ✅ True
print(s.searchMatrix(matrix, 1))    # ✅ True
print(s.searchMatrix(matrix, 100))  # ✅ False