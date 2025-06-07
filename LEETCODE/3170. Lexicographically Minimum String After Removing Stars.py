from heapq import heappop, heappush


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        for i,c in enumerate(s):
            if c == "*":
                heappop(heap)
            else:
                heappush(heap, (c,-i))

        ans = ['' for _ in range(len(s))]
        while heap:
            c,i = heappop(heap)
            ans[-i] = c
        return ''.join(ans)