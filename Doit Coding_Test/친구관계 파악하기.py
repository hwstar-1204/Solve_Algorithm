#친구관계 파악하기 
"""
n: 사람의 수 
m: 친구 관계의 수 
visited: 방문 기록 저장 리스트 
arrive: 도착 확인 변수 

#DFS 구현
DFS(현재 노드, 깊이):
    if 깊이가 5:
        arrive = true
        함수 종료 
    방문 리스트에 현재 노드 방문 기록
    현재 노드의 연결 노드중 방문하지 않은 노드로 DFS 실행: #호출마다 depth는 1씩 증가 

for M의 개수만큼 반복:
    A인접 리스트에 그래프 데이터 저장 

for n의 개수만큼 반복:
    노드마다 DFS실행 
    if arrive:
        반복문 종료 

if arrive:
    1출력
else:
    0출력 
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m = map(int,input().split())
arrive = False
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(now,depth):
    global arrive
    if depth == 5:
        arrive = True
        return 
    visited[now] = True
    for i in a[now]:
        if not visited[i]:
            DFS(i,depth+1)
    visited[now] = False #현재 노드에서 다 들어갔다 나왓으면 현재 노드 방문 취소 

for _ in range(m):
    s,e = map(int,input().split())
    a[s].append(e) #무방향 그래프 
    a[e].append(s)

for i in range(n+1):
    DFS(i,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)