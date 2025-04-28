from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(curr_s_list: List[str], start_idx: int):
            if start_idx == len(s):
                ans.append(curr_s_list)                
                return

            for end_idx in range(start_idx, len(s)):
                sub_s = s[start_idx:end_idx+1]
                if sub_s != sub_s[::-1]: continue

                curr_s_list.append(sub_s)
                backtrack(curr_s_list, end_idx+1)
                curr_s_list.pop()

        backtrack([], 0)
        return ans
