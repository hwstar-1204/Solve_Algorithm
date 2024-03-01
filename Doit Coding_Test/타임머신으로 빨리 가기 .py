#타임머신으로 빨리 가기 
"""
n: 노드 개수, m: 에지 개수 
edges: 에지 정보 저장 리스트 
distance: 거리 리스트 

for 에지 개수만큼 반복:
    에지 리스트에 에지 정보 저장 

#밸먼 포드 수행
거리 리스트에 출발 노드 0으로 저장 

for 노드 개수-1만큼 반복:
    for 에지 개수만큼 반복:
    현재 에지 데이터 가져오기 
    if 출발 노드가 무한대가 아니고 종료 노드값 > 출발노드값 + 에지 가중치:
        업데이트 수행 
    
for 에지 개수만큼 반복:
    현재 에지 데이터 가져오기 
    if 출발 노드가 무한대가 아니고 종료 노드값 < 출발 노드값 + 에지 가중치:
        업데이트 가능하므로 음의 사이클 존재 

음의 사이클 미존재하면 거리리스트 출력
음의 사이클 존재하면 -1
"""

# import sys
# input = sys.stdin.readline
# n,m = map(int,input().split())
# edges = []
# distance = [sys.maxsize] * (n+1)

# for i in range(m): #에지 리스트 
#     start,end,time = map(int,input().split())
#     edges.append((start,end,time))

# #밸먼 포드 수행 
# distance[1]=0 #출발 노드 0으로 초기화 

# for _ in range(n-1):
#     for start,end,time in edges:
#         if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
#             distance[end] = distance[start] + time

# #음의 사이클 여부 확인
# mycycle = False
# for start,end,time in edges:
#     if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
#         mycycle = True

# if not mycycle:
#     for i in range(2,n+1):
#         if distance[i] != sys.maxsize:
#             print(distance[i])
#         else:
#             print(-1)
# else:
#     print(-1)

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
edges = []
distance = [sys.maxsize] *(n+1)

for _ in range(m): #에지 리스트 초기화 
    start,end,time = map(int,input().split())
    edges.append((start,end,time))

#밸먼포드 수행
distance[1] = 0 #출발점 초기화 

for _ in range(n-1): #노드-1 번 반복 
    for start,end,time in edges: #모든 간선에 대해서 
        if distance[start] != sys.maxsize and distance[end] > distance[start]+time:
            distance[end] = distance[start]+time #간선 정보 업데이트 

#음의 사이클 여부 판단
cycle = False
for start,end,time in edges: 
        if distance[start] != sys.maxsize and distance[end] > distance[start]+time:
            cycle = True
            break

if not cycle:
    for i in range(2,n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)