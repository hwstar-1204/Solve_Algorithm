import heapq
from typing import List
# heap
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = list(map(str, [i for i in range(1,n+1)]))
        heapq.heapify(nums)
        return list(map(int, [heapq.heappop(nums) for _ in range(n)]))

# DFS
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        for i in range(1, 10):
            dfs(i)
        return result

n = 13
s = Solution()
print(s.lexicalOrder(n))