from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num1 == nums[j] and (i * j) % k == 0:
                    ans += 1
        return ans

nums = [3,1,2,2,2,1,3]
k = 2
s = Solution()
res = s.countPairs(nums,k)
print(res)