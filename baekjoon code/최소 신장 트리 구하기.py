#최소 신장 트리 구하기 
"""
v,e = 노드,에지 개수 
대표노드 리스트 초기화
for e만큼 반복:
    edges 입력받기 (가중치,시작,종료) 형식으로 
엣지를 가중치에 따라 오름차순 정렬 

유니온 함수
파인드 함수 

for 노드-1만큼 반복:
    에지 데이터 가져오기 
   if find(a) == find(b):
        다음으로 넘겨 
    union(a,b)
    결과 += 가중치 

print(결과 )
"""
import sys
from queue import PriorityQueue
input = sys.stdin.readline

v,e = map(int,input().split())
parent = [i for i in range(v+1)]
queue = PriorityQueue()

for _ in range(e):
    s,e,w = map(int,input().split())
    queue.put((w,s,e))

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a] ###

def union(s,e):
    a = find(s)
    b = find(e)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b     
result = 0
sum_edges = 0
while sum_edges < v-1:
    w,s,e = queue.get()
    if find(s) != find(e):
        union(s,e)
        result += w
        sum_edges += 1

print(result)