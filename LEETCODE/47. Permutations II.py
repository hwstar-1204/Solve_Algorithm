from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        length = len(nums)
        used = [False] * length
    
        def backtrack(curr_list: List[int]):
            if length == len(curr_list):
                ans.append(list(curr_list))
                return 

            for i in range(length):
                if used[i]: continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue

                used[i] = True
                curr_list.append(nums[i])
                backtrack(curr_list)
                curr_list.pop()
                used[i] = False


        backtrack([])
        return ans