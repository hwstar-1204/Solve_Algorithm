from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, open_cnt, close_cnt):
            nonlocal ans
            if n*2 == len(s):
                ans.append(s)
                return 

            if open_cnt < n:
                backtrack(s+"(", open_cnt+1, close_cnt)
            if close_cnt < open_cnt:
                backtrack(s+")", open_cnt, close_cnt+1)
        
        backtrack("", 0, 0)
        return ans