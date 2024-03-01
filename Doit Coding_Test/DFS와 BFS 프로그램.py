#DFS와 BFS 프로그램 
"""
n: 노드 개수
m: 에지의 개수 
start: 탐색을 시작할 노드 번호 
a: 그래프 데이터 저장 인접 리스트 

for m의 개수만큼 반복:
    a인접 리스트에 그래프 데이터 저장

#방문할 수 있는 노드가 여러 개일 경우에는 번호가 가장 작은것을 먼저 방문하기 위해 정렬
for n+1만큼 반복:
    각 노드와 관련된 에지를 정렬 

#DFS 구현 
DFS:
    현재 노드 출력하기 
    visited 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS실행하기 (재귀함수)

visited 초기화 
DFS(start) #실행 

#BFS 구현
BFS:
    큐 자료구조에 시작 노드 삽입 
    visited 리스트에 현재 노드 방문 기록 
    while 큐가 빌때까지:
        큐에서 노드 가져오기 
        가져온 노드 출력 
        현재 노드의 연결 노드 중 미 방문 노드를 큐에 삽입하고 방문 노드 기록

visited 리스트 초기화 
BFS(start) #실행 
"""
from collections import deque

n,m,start = map(int,input().split())
a = [[] for _ in range(n+1)]

for _ in range(m):
    s,e = map(int,input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n+1):
    a[i].sort()

def DFS(v):
    print(v,end=' ')
    visited[v] = True
    for i in a[v]:
        if not visited[i]:
            DFS(i)

visited = [False] * (n+1)
DFS(start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')
        for i in a[now_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        

print()
visited = [False] * (n+1)
BFS(start)

    