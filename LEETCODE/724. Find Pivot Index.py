from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums) - nums[0]

        for i in range(len(nums)-1):
            if left_sum == right_sum:
                return i

            left_sum += nums[i]
            right_sum -= nums[i+1]

        if not (sum(nums) - nums[-1]):
            return len(nums) - 1

        return -1
