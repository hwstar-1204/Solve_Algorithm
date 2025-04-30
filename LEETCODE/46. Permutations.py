from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(curr_nums: List[int], curr_idx: int, visited: set[List]):
            if curr_idx == len(nums):
                ans.append(curr_nums[:])
                return 
            
            for i in range(len(nums)):
                if i in visited:  continue

                curr_nums.append(nums[i])
                visited.add(i)
                dfs(curr_nums, curr_idx+1, visited)
                visited.discard(i)
                curr_nums.pop()
            
        dfs([], 0, set([]))
        return ans
