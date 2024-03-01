#트리의 부모 찾기 
""""
N: 노드 개수 
노드개수만큼 인접리스트 초기화 

for n-1:
    연결된 노드 번호 받아서 인접리스트에 저장 
    양방향 

방문 리스트 초기화 
정답 리스트 선언 (모두 0, DFS방문할때 부모노드를 저장)
for n(노드개수):
    
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(num):
    visited[num] = True
    for next in tree[num]:
        if not visited[next]:
            answer[next] = num
            DFS(next)

DFS(1)

for i in range(2,n+1):
    print(answer[i])

#------------------연습용----------------
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = [0 for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(num):
    visited[num] = True
    for next in tree[num]:
        if not visited[next]:
            answer[next] = num 
            DFS(next)

DFS(1)
for i in range(2,n+1):
    print(answer[i])