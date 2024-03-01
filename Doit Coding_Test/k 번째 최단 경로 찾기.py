#k 번째 최단 경로 찾기 
"""
n: 노드 개수
m: 에지 개수
k: 몇번째 최단 경로를 구할지 
w: 그래프 정보 저장 인접 리스트 
distance: 거리 리스트 

for 에지 개수만큼:
    인접 리스트에 에지 정보를 저장 

우선 순위 큐에 시작 노드 저장 #1번 노드 거리 0으로 
시작 도시 최단 거리 저장 #시작점이므로 0 

#다익스트라 
while 큐가 빌때까지:
    우선순위 큐에서 데이터 가져오기 (거리,노드)
    for 현재 노드에서 연결된 에지 탐색:
        새로운 총 거리 = 현재 노드의 거리 + 에지 가중치
        if 새로운 노드이 k 번째 최단 거리 > 새로운 총 거리:
            새로운 노드의 k번째 최단거리를 새로운 총 거리로 변경하고 거리순 정렬 
            우선 순위 큐에 새로운 데이터 추가 (거리,노드)

for 노드 개수:
#다음은 최초 값이라면 k번째 거리가 없다는 뜻
    if 각 노드의 거리 리스트에 k번째 값이 최초 설정값:
        -1
    else:
        k번째 값 출력 
"""

import sys
import heapq
input = sys.stdin.readline
n,m,k = map(int,input().split())
w = [[]for _ in range(n+1)]
#거리 리스트를 충분히 큰 값으로 초기화
distance = [[sys.maxsize] * k for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    w[a].append((b,c))

pq = [(0,1)] 
distance[0][1] = 0

while pq: 
    cost, node = heapq.heappop(pq)
    for nNode, Ncost in w[node]:
        sCost = cost + Ncost
        if distance[nNode][k-1] > sCost:
            distance[nNode][k-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq,[sCost,nNode])

for i in range(1,n+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])