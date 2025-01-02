from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        height = 0
        ans = 0
        for g in gain:
            height += g
            ans = max(ans, height)

        return ans