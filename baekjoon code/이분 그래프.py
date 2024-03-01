#이분 그래프
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
k = int(input())

def DFS(idx,graph,group):
    visited[idx] = group

    for next in graph[idx]:
        if not visited[next]:
            r = DFS(next,graph,-group)
            if not r:
                return False
        else:
            if visited[idx] == visited[next]:
                return False
    return True

for _ in range(k):
    v,e = map(int,input().split()) #노드, 간선
    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    group = 1 
    result = True

    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,v+1):
        if not visited[i]:
            result = DFS(i,graph,group)
            if not result:
                break
    print("YES" if result else "NO")
