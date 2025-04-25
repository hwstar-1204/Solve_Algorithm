"""
1. 상태 유지할 값
2. 정답 조건
3. 다음 가지로 넘어갈 조건 (가지치기)
"""
from typing import List


class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(num_list: List[int], start_index: int, curr_sum: int):
            nonlocal ans
            if curr_sum > target: return
            if curr_sum == target:
                ans.append(list(num_list))
                return 
            
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                if i > start_index and candidates[i] == candidates[i-1]: 
                    continue  # 같은 depth에서 중복된 값은 건너뜀
                print(f"i: {i}, start_index: {start_index}, candidates[i]: {candidates[i]}, candidates[i-1]: {candidates[i-1]}", '\n')
                num_list.append(candidate)
                backtrack(num_list, i+1, curr_sum + candidate)
                num_list.pop()
        
        backtrack([], 0, 0)
        return ans

candidates = [10,1,2,7,6,1,5]  # 1,1,2,5,6,7,10
target = 8

s = Solution()
res = s.combinationSum2(candidates, target)
print(res)
