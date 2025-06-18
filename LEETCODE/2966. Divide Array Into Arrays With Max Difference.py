from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(0, len(nums), 3):
            start, end = i, i+2
            if nums[end] - nums[start] > k:
                return []
            ans.append(nums[start:end+1])
        
        return ans
