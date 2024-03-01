#토마토
import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
days = 0 #지난 날짜 
dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i,j))

def BFS():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

        
            if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0: #주변이 익지않은 토마토이면 
                box[nx][ny] = box[x][y]+1 
                queue.append((nx,ny))
            
BFS()
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
    days = max(days,max(box[i]))

print(days-1)