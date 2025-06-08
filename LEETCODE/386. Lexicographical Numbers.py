import heapq
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = list(map(str, [i for i in range(1,n+1)]))
        heapq.heapify(nums)
        return list(map(int, [heapq.heappop(nums) for _ in range(n)]))

        