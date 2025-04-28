from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(curr_s_list: List[str], start_idx: int):
            if sum([len(s) for s in curr_s_list]) == len(s):
                # if self.is_palindrome(curr_s_list):
                ans.append(list(curr_s_list))
                return

            for end_idx in range(start_idx, len(s)):
                sub_s = s[start_idx:end_idx+1]
                if sub_s != sub_s[::-1]: continue

                curr_s_list.append(sub_s)
                backtrack(curr_s_list, end_idx+1)
                curr_s_list.pop()

        backtrack([], 0)
        return ans

    def is_palindrome(self, s_list: List[str]) -> bool:
        for s in s_list:
            if s != s[::-1]:
                return False
        return True


s = "a"
solution = Solution()
res = solution.partition(s)
print(res)
# assert res == [["a"]]
