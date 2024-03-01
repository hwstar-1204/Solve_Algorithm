#최단 경로 구하기 
"""

"""
from queue import PriorityQueue
import sys
n,e = map(int,input().split()) #노드 수 , 간선 수 
k = int(input())
queue = PriorityQueue()

a = [[] for _ in range(n+1)] #그래프를 인접 리스트로 표현 
visited = [False] * (n+1) #방문 기록 리스트 
distance = [sys.maxsize] * (n+1) #시작노드에서 각 노드까지의 거리 리스트 

for _ in range(e): #인접 리스트 초기화 
    u,v,w = map(int,input().split())
    a[u].append((v,w))


queue.put((0,k)) #거리값을 우선순위로 정렬하므로 넣을때 0번인덱스에 넣음
distance[k] = 0

while queue.qsize()>0:
    now = queue.get()
    c_v = now[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for node in a[c_v]:
        next = node[0]
        value = node[1]
        if distance[next] > distance[c_v]+ value : #방문한적이 없고 현재까지 거리+다음 노드까지 거리 < 거리 리스트에 있는 다음 노드까지의 거리보다 작으면
            distance[next] = distance[c_v]+value
            queue.put((distance[next],next))

for i in range(1,n+1):
    if visited[i]:
        print(distance[i])
    else:
        print('INF')

