#DFS와 BFS
import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
n,m,v = map(int,input().split()) #정점, 간선, 시작점 

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

def DFS(idx,g):
    visited[idx] = True
    print(idx,end=' ')
    for next in g[idx]:
        if visited[next]:
            continue
        DFS(next,g)

def BFS(idx,g):
    queue = deque()
    queue.append(idx)
    visited[idx] = True

    while queue:
        now = queue.popleft()
        print(now,end=' ')
        
        for next in g[now]:
            if visited[next]:
                continue
            visited[next] = True
            queue.append(next)

DFS(v,graph)
for i in range(n+1):
    visited[i] = False
print()
BFS(v,graph)