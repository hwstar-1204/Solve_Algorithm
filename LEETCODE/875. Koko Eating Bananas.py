from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = ceil(sum(piles) / h), max(piles)
        # left, right = 1, max(piles)

        while left < right:
            k = (left+right) // 2
            total = sum([ceil(p / k) for p in piles])
            if total > h:
                left = k + 1
            else:
                right = k
        return left
