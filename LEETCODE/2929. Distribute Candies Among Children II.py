# Implement 
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(n, limit) + 1):
            low = max(0, n-limit-i)
            high = min(limit, n-i)
            if low <= high:
                ans += (high-low+1)
        return ans


# backtracking (Time Limit Exceeded)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:

        def backtrack(remain: int, level: int):
            if level == 3:
                return 1 if remain == 0 else 0
            
            cnt = 0
            for i in range(min(limit, remain) + 1):
                cnt += backtrack(remain - i, level + 1)
            return cnt

        return backtrack(n,0)
    