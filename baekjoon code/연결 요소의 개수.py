#연결 요소의 개수 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
n,m = map(int,input().split()) #정점, 간선 

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(idx):
    visited[idx] = True
    for next in graph[idx]:
        if not visited[next]:
            DFS(next)

def dfs(idx):
    stack = []
    stack.append(idx)
    while stack:
        now = stack.pop()
        visited[now] = True
        for next in graph[now]:
            if not visited[next]:
                stack.append(next)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)

    
#테스트 케이스 
"""
1 2 5
3 4 6 7
7 6
"""