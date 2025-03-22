"""
문제 유형 : 그리디, 힙, 정렬
정렬 후 한 번에 가져오는 것이 아니라, 최적의 조합을 찾으면서 탐색하며 최대값을 갱신하는 방식
✅ 그리디하게 nums2의 큰 값부터 선택 (매 순간 큰값들 중 작은값이 선택됨)
✅ 힙을 사용해 nums1의 합을 최적으로 유지
✅ 매 순간 최댓값을 갱신하면서 탐색

시간 복잡도: O(NlogN + NlogK) - 정렬 + 최소힙 유지
"""

from heapq import heappush, heappop
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1_sum, max_score = 0, 0
        min_heap = []
        
        nums = sorted(zip(nums1, nums2), key=lambda x: (x[1]), reverse=True)
        for n1, n2 in nums:
            heappush(min_heap, n1)
            n1_sum += n1

            if len(min_heap) > k:
                n1_sum -= heappop(min_heap)
            
            if len(min_heap) == k:
                max_score = max(max_score, n1_sum * n2)

        return max_score
