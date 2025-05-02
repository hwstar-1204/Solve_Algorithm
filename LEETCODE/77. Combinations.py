from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1,n+1)]

        def backtrack(curr_list: List[int], curr_idx):
            if len(curr_list) == k:
                ans.append(list(curr_list))
                return 

            for i in range(curr_idx, n):
                curr_list.append(nums[i])
                backtrack(curr_list, i+1)
                curr_list.pop()

        backtrack([], 0)
        return ans