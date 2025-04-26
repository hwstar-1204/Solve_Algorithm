from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(curr_nums: List[str], start_idx: int):
            nonlocal ans
            if len(curr_nums) > 4:
                return 
            if len(curr_nums) == 4 and start_idx == len(s):
                ans.append(".".join(curr_nums))
                return

            for i in range(1,4):
                if start_idx + i > len(s):
                    break
                num = s[start_idx:start_idx+i]
                if not num or int(num) > 255 or (num.startswith('0') and len(num) > 1):
                    continue
                
                curr_nums.append(num)
                backtrack(curr_nums, start_idx+i)
                curr_nums.pop()


        backtrack([], 0)
        return ans
