from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        min_num = nums[0]
        for num in nums[1:]:
            if min_num < num:
                max_diff = max(max_diff, num - min_num)
            else:
                min_num = num
        return max_diff
