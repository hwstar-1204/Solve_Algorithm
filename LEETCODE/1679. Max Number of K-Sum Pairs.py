from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        left, right = 0, len(nums) - 1
        nums.sort()

        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                left += 1
            elif total > k:
                right -= 1
            else:
                left += 1
                right -= 1
                answer += 1
        return answer