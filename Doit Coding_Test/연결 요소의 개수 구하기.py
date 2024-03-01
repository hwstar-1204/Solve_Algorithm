#연결 요소의 개수 구하기 
"""
n: 노드 개수
m: 에지 개수 
a: 그래프 데이터 저장 인접 리스트 초기화 
visited: 방문기록 초기화 

#DFS 구현 
DFS:
    visited 리스트에 현재 노드 방문 기록 
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행 (재귀함수)

for m의 개수만큼 반복:
    a 인접 리스트에 그래프 데이터 저장 

for n의 개수만큼 반복:
    if 방문하지 않은 노드가 있으면:
        연결 요소 개수 값 1증가 
        DFS 실행 

연결 요소 개수 값 출력 
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int, input().split())
a = [[] for i in range(n+1)]
visited = [False] * (n+1) 

def DFS(v):
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s,e = map(int,input().split())
    a[s].append(e)
    a[e].append(s)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
