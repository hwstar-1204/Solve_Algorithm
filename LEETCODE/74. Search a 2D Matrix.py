from typing import List


class Solution:
    # O(log(m) + log(n))
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

    # O(log(m*n)) 
    # 위와 시간복잡도는 같음
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n-1
        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
