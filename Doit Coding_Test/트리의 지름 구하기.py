#트리의 지름 구하기 
"""
n: 노드 개수
a: 그래프 데이터 저장 인접 리스트 

for n만큼 반복:
    a인접 리스트에 그래프 데이터 저장 

visited 리스트 초기화 
distance 리스트 초기화 

#BFS 구현
BFS:
    큐 자료구조에 시작 노드 삽입 
    visited 리스트에 현재 노드 방문 기록 
    while 큐가 비어있을때까지:
        큐에서 노드 데이터를 가져오기 
        for 현재 노드의 연결노드:
            if 미 방문 노드:
                큐에 데이터 삽입 
                visited 리스트에 방문 기록 
                큐에 삽입된 노드 거리 = 현재 노드의 거리 + 에지의 가중치로 변경 

BFS (임의의 점을 시작점으로) 실행
distance 리스트에서 가장 큰 값을 지닌 노드를 시작점으로 지정
visited 리스트 초기화 
distance 리스트 초기화 
BFS(새로운 시작점으로) 실행 
distance 리스트에서 가장 큰 수를 정답으로 출력 
"""

from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]

for _ in range(n):
    data = list(map(int,input().split()))
    index = 0
    s = data[index]
    index += 1
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        a[s].append((e,v))
        index += 2

distance = [0] * (n+1)
visited = [False] * (n+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in a[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

BFS(1)
max = 1
for i in range(2,n+1):
    if distance[max] < distance[i]:
        max = i 

distance = [0] * (n+1)
visisted = [False] * (n+1)
BFS(max)
distance.sort() #오름차순 정렬 
print(distance[n]) #가장 큰값 출력