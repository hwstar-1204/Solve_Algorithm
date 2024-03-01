#최소 공통 조상 구하기 1 
"""
n: 노드개수 ,m: 질의 개수 
그래프를 저장할 인접 리스트
길이 저장할 리스트
방문여부 리스트 

for n+1:
    두 노드 정보를 인접리스트에 추가 

DFS(index,depth):
   인덱스 방문표시 
   인덱스 깊이 저장 
   for 다음 노드들에 대해서 
        방문하지않았다면 
            자신의 부모노드 저장 
            깊이++ 
            DFS(다음노드)
            다음노드 방문 표시 해제 

LCA(a,b):
    a와 b의 깊이 대소 비교 
    깊이가 큰것을 작은것과 맞춘다. 
    while a != b:
        b = parent[b]
    
    깊이를 다 맞추고 값을 비교했을때 같으면 최소공통조상 찾음 
    아니면 한칸씩 동시에 올리면서 부모노드의 값이 같을떄 까지 올린다. 
    while a !=b:
        a = parent[a]
        b = parent[b]

    두값중 하나를 정답으로 반환 

"""
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n+1)]
d = [0] * (n+1)
parent = [0] * (n+1)
visited = [False] *(n+1)

for _ in range(n-1):
    n1,n2 = map(int,input().split())
    g[n1].append(n2)
    g[n2].append(n1)

def DFS(idx,depth):
    visited[idx] = True
    d[idx] = depth
    for next in g[idx]:
        if visited[next]:
            continue
        parent[next] = idx
        DFS(next,depth+1)

def LCA(a,b):
    a, b = (a, b) if d[a] < d[b] else (b, a) #b의 깊이가 더 큰걸로
    # if d[a] < d[b]:
    #     temp = a
    #     a = b
    #     b = temp

    while d[a]!=d[b]:
        b = parent[b]

    while a!=b:
        a = parent[a]
        b = parent[b]
    return a

DFS(1,0) 
print(parent)
m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(LCA(a,b))



#----------------------------------
from collections import deque

def BFS(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    depth = 1
    now_size = 1
    count = 0
    while queue:
        now_node = queue.popleft()
        for next in g[now_node]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)
                parent[next] = now_node
                d[next] = depth
        count += 1
        if count == depth:
            count = 0
            now_size = len(queue)
            depth += 1
