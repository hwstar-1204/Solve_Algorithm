from collections import deque
from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans= 0

        while nums:
            if len(set(nums)) == len(nums): break
            
            length = 3 if len(nums) > 2 else len(nums)
            nums = nums[length:]
            ans += 1
        
        return ans
