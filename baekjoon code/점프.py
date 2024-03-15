#점프 
"""
N*N 게임판 가장 왼쪽 위에서 가장 오른쪽 아래칸으로 규칙에 맞게 점프 
각 칸: 현재칸에서 갈 수 있는 거리 
반드시 오른쪽 or 아래 이동 
0이 종착점 

입력: 게임보드는 4<=n<=100 점프 가능거리는 0보다 크거나같고 9보다 작거나 같음
마지막은 항상 0 
출력: 가장 왼쪽위에서 가장 오른쪽 아래까지 가는 경로 수 
///
2 3 3 1
1 2 1 3
1 2 3 1
3 1 1 0

0 0 1 0
0 0 0 0
1 1 0 1
1 0 1 3

보드내에 있는 범위인지 확인하는 함수(board,x,y,jump)
    0<= x,y < n

스택에 시작점에서 갈 수 있는 자리 추가 
while 스택이 빌떄까지 반복:
    x,y = 스택에서 뽑은자리 
    
    # 아래이동 가능한지
    if x + 자기자신값 했을때 움직일수 있는 범위이면 
        그자리 +1 
        그자리 스택에 추가

    # 오른쪽으로 이동 가능한지 

마지막 자리 출력 

"""
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**7)
# n = int(input())
# board = [list(map(int,input().split())) for _ in range(n)]
# dp = [[0] * n for _ in range(n)]

# stack = [] #탐색할 위치 튜플 저장 
# first = board[0][0]
# stack.append((0,first)) #오른쪽 이동 
# stack.append((first,0)) #아래 이동 

# while stack:
#     x,y = stack.pop()
#     # 목적지 도착
#     if not board[x][y]:  
#         continue

#     down = x+board[x][y]
#     right = y+board[x][y]
#     #아래,오른쪽 이동가능여부
#     if down < n:
#         dp[down][y] += 1
#         stack.append((down,y))
#     if right < n:
#         dp[x][right] += 1
#         stack.append((x,right))

# print(dp[n-1][n-1])


#//--------------------------------//

import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        now = board[x][y]

        if x == y == n-1:
            print(dp[x][y])
            break

        down = x + now
        right = y + now

        if down < n:
            dp[down][y] += dp[x][y]
        if right < n:
            dp[x][right] += dp[x][y]

for d in dp:
    print(*d)