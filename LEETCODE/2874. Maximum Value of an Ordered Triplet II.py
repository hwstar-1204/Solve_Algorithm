from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])

        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])

        for j in range(1, n-1):
            diff = prefix_max[j-1] - nums[j]
            ans = max(ans, diff * suffix_max[j+1])

        return ans
