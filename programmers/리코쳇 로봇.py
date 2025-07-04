""" 
. : 빈공간, D : 장애물, R : 로봇처음 위치, G : 목표지점 
"""
from collections import deque


def solution(board):    
    n, m = len(board), len(board[0])
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # 시작, 종료 위치 찾기 
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i, j)
            elif board[i][j] == "G":
                goal = (i, j)
            
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    q = deque()
    
    # 시작점에서 갈 수 있는 경우 4가지 추가 
    for d in range(4):
        q.append((start[0], start[1], d, 0))  # x, y, 방향, 이동 횟수
        visited[start[0]][start[1]][d] = True
    
    while q:
        x,y, d, cnt = q.popleft()
        
        if (x,y) == goal:
            return cnt
        
        dx, dy = directions[d]
        nx, ny = x, y
        
        # 장애물 도달까지 직진
        while True:
            tx, ty = nx + dx, ny + dy
            if 0 <= tx < n and 0 <= ty < m and board[tx][ty] != "D":
                nx, ny = tx, ty
            else:
                break

        # 장애물 앞에서 방향 전환
        for nd in range(4):
            if not visited[nx][ny][nd]:
                q.append((nx, ny, nd, cnt+1))
                visited[nx][ny][nd] = True
        
    return -1
