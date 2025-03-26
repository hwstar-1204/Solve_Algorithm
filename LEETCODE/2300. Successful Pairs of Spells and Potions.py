from typing import List
from bisect import bisect_left
from math import ceil


# 이분탐색 구현한것으로 적용
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        m = len(potions)

        potions.sort()

        for spell in spells:
            left, right = 0, m - 1
            while left <= right:
                mid = (left + right) // 2
                strength = potions[mid] * spell
                if strength >= success:
                    right = mid - 1
                elif strength < success:
                    left = mid + 1

            ans.append(m - right - 1)

        return ans

# 이분탐색 라이브러리 사용 (m+n)log(n)
# potions의 각 요소에 spell을 곱해서 potion * spell >= success 계산하는 것 개선
# potion >= success / spell
# success / spell 이 값이 계산되지 않은 potions에서 어디에 위치하는지 확인
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()  # mlog(m)

        for spell in spells:  # nlog(n)
            place = bisect_left(potions, (ceil(success / spell)))
            ans.append(len(potions) - place)

        return ans

    