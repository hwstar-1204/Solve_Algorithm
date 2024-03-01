#최소 공통 조상 구하기 2
"""

"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
d = [0]*(n+1)
# parent 

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

temp = 1
kmax = 0
while temp <= n:
    temp <<= 1
    kmax += 1

parent = [[0 for j in range(n+1)] for _ in range(kmax+1)]

def DFS(idx,depth):
    visited[idx] = True
    d[idx] = depth
    for next in tree[idx]:
        if visited[next]:
            continue
        parent[0][next] = idx
        DFS(next,depth+1)

DFS(1,0)

for k in range(1,kmax+1):
    for n in range(1,n+1):
        parent[k][n] = parent[k-1][parent[k-1][n]]

def LCA(a,b):
    a,b = (a,b) if d[a]<d[b] else (b,a)

    #깊이 빠르게 맞추기 
    for k in range(kmax,-1,-1): 
        if pow(2,k) <= d[b]-d[a]:
            if d[a] <= d[parent[k][b]]:
                b = parent[k][b]
    #조상 빠르게 찾기 
    for k in range(kmax,-1,-1):
        if a==b: 
            break
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    LCA = a
    if a!= b:
        LCA = parent[0][LCA]
    return LCA 