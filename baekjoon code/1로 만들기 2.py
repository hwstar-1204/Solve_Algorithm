"""
3가지 연산으로 1만드는 최소 횟수 구하기 
1. x를 3으로 나누기 
2. x를 2로 나누기 
3. 1 빼기 

1 <= n < 10^6
"""

# BFS (시간 초과)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque()
q.append([n])

while q:
    arr = q.popleft()
    x = arr[0]

    if x == 1:
        break
    if x % 3 == 0:
        q.append([x//3] + arr)
    if x % 2 == 0:
        q.append([x//2] + arr)
    q.append([x-1] + arr)

print(len(arr) - 1)
print(*arr[::-1])


# DP
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    if i % 3 == 0:
        if dp[i][0] > dp[i//3][0] + 1:
            dp[i][0] = dp[i//3][0] + 1
            dp[i][1] = dp[i//3][1] + [i]
    if i % 2 == 0:
        if dp[i][0] > dp[i//2][0] + 1:
            dp[i][0] = dp[i//2][0] + 1
            dp[i][1] = dp[i//2][1] + [i]
print(dp[n][0])
print(*dp[n][1][::-1])