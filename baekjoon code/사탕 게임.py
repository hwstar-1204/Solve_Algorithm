import sys
import copy
input = sys.stdin.readline

n = int(input())
color_mapping = {'C': 0, 'P': 1, 'Z': 2, 'Y': 3}
board = [[color_mapping[c] for c in input().rstrip()] for _ in range(n)]
max_c = 1

def eatCandy(tb):
    mc = 1
    for i in range(n):
        #가로
        cnt = 1
        for s in range(1,n):
            if tb[i][s] == tb[i][s-1]:
                cnt += 1
            else:
                cnt = 1
            mc = max(mc,cnt)
        #세로
        cnt = 1
        for s in range(1,n):
            if tb[s][i] == tb[s-1][i]:
                cnt += 1
            else:
                cnt = 1
            mc = max(mc,cnt)
    return mc 

for i in range(n):
    for j in range(n):
        #가로
        if j+1 < n:
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
            cx = eatCandy(board)
            max_c = max(max_c,cx)
            board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        #세로
        if i+1<n:
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
            cy = eatCandy(board)
            max_c = max(max_c,cy)
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]

print(max_c)