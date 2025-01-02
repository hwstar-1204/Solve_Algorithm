from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        k = 1
        ans = []

        for end in range(len(nums)):
            if not nums[end]:
                k -= 1

            if k < 0:
                if not nums[start]:
                    k += 1
                start += 1

            ans.append(end-start)
        
        print(ans)
        return end - start
    