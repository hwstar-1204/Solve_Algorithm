# 바이러스
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input()) # 컴퓨터수
v = int(input()) # 간선 수 

visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(v):
    s, e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

answer = 0        
def DFS(node):
    global answer 
    visited[node] = True
    answer += 1
    
    for next_node in graph[node]:
        if not visited[next_node]:
            DFS(next_node)
    return answer
print(DFS(1)-1)