from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = set()
        right = 0
        
        for mid in range(len(nums)):
            if nums[mid] == key:
                left, right = max(right, mid-k), min(mid+k+1, len(nums))
                ans.update(range(left, right))

        return list(ans)