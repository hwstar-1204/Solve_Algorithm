#지뢰 찾기 
import sys
input = sys.stdin.readline

n = int(input())
bomb = [list(input().rstrip()) for _ in range(n)]
board = [list(input().rstrip()) for _ in range(n)]
flag = False

def search_bomb(bb,row,col):
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0,-1,-1,-1]

    cnt_b = 0 # 주변 폭탄 개수
    for x,y in zip(dx,dy):
        mx = row+x
        my = col+y
        if mx < 0 or my < 0 or mx >= n or my >= n:
            continue
        if bb[mx][my] == '*':
            cnt_b += 1
    return cnt_b

for i in range(n):
    for j in range(n):
        if board[i][j] == 'x':
            if bomb[i][j] == '*':
                flag = True # 지뢰가 있으면서 열린곳 
                continue
            board[i][j] = str(search_bomb(bomb,i,j))
if flag:
    for i in range(n):
        for j in range(n):
            if bomb[i][j] == '*':
                board[i][j] = '*'

for b in board:
    print(''.join(b))