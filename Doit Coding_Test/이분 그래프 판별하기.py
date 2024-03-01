#이분 그래프 판별하기 
"""
n: 테스트 케이스 개수 
iseven: 이분 그래프 판별 변수

#DFS
DFS:
    visited 리스트에 현재 노드 방문 기록하기 
    if 현재 노드의 연결 노드 중 방문하지 않은 노드:
        현재 노드와 다른 집합으로 연결 노드 집합 저장
        DFS(다음 노드)
    elif 이미 방문한 노드인데 현재 나의 노드와 같은 집합:
        이분 그래프 아님 

for n만큼 반복:
    v: 노드 개수
    e: 에지 개수 
    a: 그래프 데이터 저장 인접 리스트 
    visited: 방문기록 저장 리스트 
    check: 노드별 집합 저장 리스트 

    iseven = true

    for e만큼 반복:
        a 인접 리스트에 그래프 데이터 저장 

    for v만큼 반복:
        각 노드에서 DFS실행 -> 결과가 이분 그래프 아니면 반복 종료 

    이분 그래프 여부 출력 
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
iseven = True

def DFS(node):
    global iseven 
    visited[node] = True
    for i in a[node]:
        if not visited[i]:
            check[i] = (check[node]+1)%2
            DFS(i)
        elif check[node] == check[i]:
            iseven = False


for _ in range(n):
    v,e = map(int,input().split())
    a = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    iseven = True

    for i in range(e):
        start,end = map(int,input().split())
        a[start].append(end)
        a[end].append(start)

    for i in range(v):
        if iseven:
            DFS(i)
        else:
            break

    if iseven:
        print("yes")
    else:
        print("No")