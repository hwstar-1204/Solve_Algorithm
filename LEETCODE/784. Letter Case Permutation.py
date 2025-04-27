from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(curr_s, curr_idx):
            if len(s) == len(curr_s):
                ans.append(curr_s)
                return

            now_s = s[curr_idx]
            backtrack(curr_s + now_s, curr_idx + 1)
            if now_s.isalpha():
                backtrack(curr_s + now_s.swapcase(), curr_idx + 1)
                

        backtrack("", 0)
        return ans
