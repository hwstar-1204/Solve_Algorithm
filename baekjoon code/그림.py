"""
그림은 1로 연결되어 이루어짐
1. 그림의 개수 출력
2. 그림의 가장 넓이가 넓은것의 넓이 출력
(그림이 하나도 없으면 0 출력)

가로(m), 세로(n) : 1 <= n,m <= 500
"""
import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())  # 가로 : m, 세로 : n
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
moves = [(0,1), (1,0), (-1,0), (0,-1)]
pic, largest = 0, 0

def BFS(row, col, visited):
    cnt = 1
    visited[row][col] = True

    q = deque([(row, col)])
    while q:
        nr, nc = q.popleft()

        for mr, mc in moves:
            next_r, next_c = nr + mr, nc + mc
            if 0 <= next_r < n and 0 <= next_c < m:
                if board[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True
                    cnt += 1
    return cnt

for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            largest = max(largest, BFS(i, j, visited))
            pic += 1

print(pic)
print(largest)
