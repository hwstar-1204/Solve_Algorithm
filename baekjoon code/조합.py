#조합
"""
0
0 1
0 2 1
0 3 3 1
0 4 6 4 1

c[n][m] = c[n-1][m-1] + c[n-1][m]  (n번)

(n+1)*(n+1) 2차원 배열 

초기화:
1. c[n][0] = 0 for(n+1)
2. c[n][n] = 1 for(1,n+1)
3. c[n][1] = n 
"""

n,m = map(int,input().split())

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][i] = 1
    dp[i][1] = i 

for i in range(3,n+1):
    for j in range(2,m+1):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][m])