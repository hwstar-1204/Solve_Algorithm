# #단지번호붙이기 
# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# map = [[] for _ in range(n)]

# for i in range(n):
#     mi = list(input().rstrip())
#     for p in mi:
#         map[i].append(int(p))

# def bfs(map,x,y):
#     queue = deque()
#     queue.append((x,y))
#     map[x][y] = 0
#     cnt = 1

#     while queue:
#         x,y = queue.popleft()
        
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if nx < 0 or nx >=n or ny < 0 or ny >= n:
#                 continue

#             if map[nx][ny] == 1:
#                 map[nx][ny] = 0
#                 queue.append((nx,ny))
#                 cnt += 1
#     return cnt 

# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# cnt = []

# for i in range(n):
#     for j in range(n):
#         if map[i][j] == 1:
#             cnt.append(bfs(map,i,j))

# cnt.sort()
# print(len(cnt))
# print(*cnt,sep='\n')
#------------------------

    



#------------------------

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [ list(map(int,input().rstrip())) for _ in range(n)]

count = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt 

def DFS(graph,x,y):
    cnt = 1
    graph[x][y] = 0

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if (0<=nx<n and 0<=ny<n) and (graph[nx][ny] == 1):
            cnt += DFS(graph,nx,ny)
    return cnt 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count.append(DFS(graph,i,j))
count.sort()
print(len(count))
print(*count,sep='\n')