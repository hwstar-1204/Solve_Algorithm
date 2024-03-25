# 최소 스패닝 트리 (프림) -> 시간 초과 O(V^2)
"""
그래프가 주어졌을때 그 그래프의 최소 스패닝 트리 구하기 
MST: 모든 정점을 연결하는 부분 그래프 중 그 가중치의 합이 최소인 트리 ,사이클 X

A -> B (가중치: C (음수일 수도 있음)
정점 개수: V ( 1 <= V <= 10000)
간선 개수: E ( 1 <= E <= 100000)

출력: MST 가중치 출력 

sudo
graph = 각 정점을 키로하고 그래프 간선 정보를 우선순위큐에 저장한 값으로 이루어진 딕셔너리 

# parent = 각 노드의 부모노드 저장 리스트 

def add_Edge(시작점,도착점,가중치)
    graph[시작점].heappush((가중치,도착점))

def prim(num):
    MST_Cost = 최소 가중치 합 저장 
    visited = 방문한 정점을 저장할 set()

    while 선택 정점의 우선순위큐에 값이 없을때까지:
        가중치, 끝점 = 선택 정점 우선순위큐.heappop
        if 끝점이 아직 방문하지 않았다면:
            끝점 방문 표시 
            최소 가중치 합에 가중치 저장 
        
        for 끝점에서 다음 후보 노드가 들어있는 우선순위큐:
            가중치, 다음 후보노드의 끝점 = 끝점 우선순위큐.heappop()
            if 다음 후보노드의 끝점이 아직 방문하지 않았다면:
                    선택정점 우선순위 큐에 추가 
    
    return value

    
# 그래프 간선 저장
for E개수 만큼:
    add_Edge(a,b,c)

print(prim(1))
"""

import sys
import heapq
input = sys.stdin.readline

V,E = map(int,input().split()) # 정점 수, 간선 수
graph = { i: [] for i in range(V+1)}

def prim(graph,start):
    MST_Cost = 0 # 그래프 최소 가중치의 합 
    visited = [False] * (V+1)
    min_heap = [(0,start)]
    while min_heap:
        w,e = heapq.heappop(min_heap)
        if not visited[e]:
            visited[e] = True
            MST_Cost += w

        for next_w, next_e in graph[e]:
            if not visited[next_e]:
                heapq.heappush(min_heap,(next_w, next_e))
    
    return MST_Cost


# 간선 정보 저장
for _ in range(E):
    s,e,weight= map(int,input().split())
    graph[s].append((weight,e))
    graph[e].append((weight,s))

print(prim(graph,1))