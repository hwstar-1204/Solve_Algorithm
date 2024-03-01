#효율적인 해킹
"""
n: 노드 개수 
m: 에지 개수 
answer: 정답 리스트 

#BFS
BFS:
    큐 자료구조에 시작 노드 삽입 
    visited 리스트에 현재 노드 방문 기록
    while 큐가 비어 있을 때까지:
        큐에서 데이터 가져오기 
        if 현재 노드의 연결 노드 중 미 방문 노드:
            visited리스트 노드 방문 기록
            신규 노드 index의 정답 리스트값 증가 
            큐에 노드 삽입 

for m만큼 반복:
    a 인접 리스트에 그래프 데이터 저장

for i 1~n:
    visited 초기화
    BFS(i) 실행 

for i 1~n:
    answer 리스트에서 가장 큰수 찾기 

for i 1~n:
    answer리스트에서 max값과 같은 값을 가진 Index를 정답으로 출력 
""" 

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
a = [[] for _ in range(n+1)]
answer = [0] * (n+1)

#BFS
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                queue.append(i)

for _ in range(m):
    s,e = map(int,input().split())
    a[s].append(e)

for i in range(1,n+1):
    visited = [False] * (n+1)
    BFS(i)

maxval = 0

for i in range(1,n+1):
    maxval = max(maxval,answer[i])

for i in range(1,n+1):
    if maxval == answer[i]:
        print(i,end=' ')