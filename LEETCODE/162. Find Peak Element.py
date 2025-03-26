from typing import List

# O(n)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return 0
        for i in range(length-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                return i
        return length - 1


# O(log(n))
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left
