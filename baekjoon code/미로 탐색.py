#미로 탐색 
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
visited = [[False]*(m+1) for _ in range(n+1)] 
for i in range(1,n+1):
    temp = list(map(int,input().strip()))
    for j in range(1,m+1):
        graph[i][j] = temp[j-1]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

queue = deque()
queue.append((1,1,1))

while queue:
    x,y,depth = queue.popleft()
 
    if x == n and y == m:
        print(depth)
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0>nx or nx>n or 0>ny or ny>m:
            continue
        # if (0<nx<=n) and (0<ny<=m):
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            queue.append((nx,ny,depth+1))