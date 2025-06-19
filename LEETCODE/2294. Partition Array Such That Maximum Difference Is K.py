from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        groups, min_vl = 0, nums[0]
        for n in nums:
            if n - min_vl > k:
                min_vl = n
                groups += 1

        return groups+1