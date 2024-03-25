# 최소 스패닝 트리 (크루스컬)
"""
그래프가 주어졌을때 그 그래프의 최소 스패닝 트리 구하기 
MST: 모든 정점을 연결하는 부분 그래프 중 그 가중치의 합이 최소인 트리 ,사이클 X

A -> B (가중치: C (음수일 수도 있음)
정점 개수: V ( 1 <= V <= 10000)
간선 개수: E ( 1 <= E <= 100000)

출력: MST 가중치 출력 

sudo
graph = 그래프 간선 정보를 저장할 리스트 
parent = 각 노드의 부모노드 저장 리스트 
def add_Edge(a,b,c)

def union:

def find:

def kruskal():
    value = 최소 가중치 합 저장 

    while 방문한 정점의 개수 <= V-1:

    
# 그래프 간선 저장
for E개수 만큼:
    add_Edge()


"""
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline 
V,E = map(int,input().split()) # 정점 수, 간선 수

graph = []
parent = [i for i in range(V+1)]

def add_edge(s,e,c):
    graph.append((s,e,c))

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

def kruskal():
    min_value = 0 # MST 최소 가중치 합 
    e = 0 #선택한 간선 수 
    idx = 0
    graph.sort(key=lambda x: x[2])

    while e < V-1 and idx < E:
        a,b,c = graph[idx]
        idx += 1
        if find(a) != find(b):
            union(a,b)
            e += 1
            min_value += c

    return min_value

# 그래프 정보 저장 
for _ in range(E):
    a,b,c = map(int,input().split())
    add_edge(a,b,c)

#크루스컬 알고리즘 수행 
answer = kruskal()
print(answer)