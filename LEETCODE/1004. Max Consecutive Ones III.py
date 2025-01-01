class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        longest = 0

        for end in range(len(nums)):
            if not nums[end]:
                k -= 1

            if k < 0:
                if not nums[start]:
                    k += 1
                start += 1

        return end - start + 1
