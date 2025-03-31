from typing import List

# 백트래킹
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        if n < sum([i for i in range(1, k+1)]):
            return ans
        
        def backtrack(start, path, target):
            if len(path) > k:
                return 

            if len(path) == k:
                if target == 0:
                    ans.append(path[:])
                return 
            
            for num in range(start, 10):
                if target < num:
                    break

                path.append(num)
                backtrack(num + 1, path, target - num)
                path.pop()
        backtrack(1, [], n)
        return ans

k = 3
n = 7
s = Solution()
res = s.combinationSum3(k, n)
print(res)
