#특정 거리의 도시 찾기 
"""
n: 노드 개수 
m: 에지 개수 
k: 목표 거리
x: 시작점
answer: 정답 리스트
visited: 방문 거리 저장 리스트 (-1로 초기화)

#BFS 구현하기
BFS:
    큐 자료구조에 시작시 노드 삽입
    visited 리스트에 현재 노드 방문 기록 #거리 저장 형태로 1증가
    while 큐가 비어있을떄까지:
        큐에서 노드 가져오기 
        if 현재 노드의 연결 노드중 방문하지 않은 노드:
            visited 리스트 값 1 증가 
            큐에 노드 삽입 

for m만큼 반복:
    a 인접 리스트에 그래프 데이터 저장 

BFS(x) 실행 

for n만큼 반복:
    방문거리가 k인 노드의 숫자를 정답리스트에 더하기 

정답 리스트 오름차순 정렬 후 순차 출력 
"""
import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
a = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1)

#BFS
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if visited[i] == -1:
                visited[i] = visited[now_node] + 1
                queue.append(i)

for i in range(m):
    s,e = map(int,input().split())
    a[s].append(e)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    print(*answer,end='\n')