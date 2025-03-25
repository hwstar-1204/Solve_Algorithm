import heapq
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        total = 0
        left_idx, right_idx = 0, len(costs) - 1
        left, right = [], []

        while k > 0:
            while len(left) < candidates and left_idx <= right_idx:
                heapq.heappush(left, costs[left_idx])
                left_idx += 1
            while len(right) < candidates and left_idx <= right_idx:
                heapq.heappush(right, costs[right_idx])
                right_idx -= 1

            left_cost = left[0] if left else float("inf")
            right_cost = right[0] if right else float("inf")

            if left_cost <= right_cost:
                total += left_cost
                heapq.heappop(left)
            else:
                total += right_cost
                heapq.heappop(right)

            k -= 1
        return total 
