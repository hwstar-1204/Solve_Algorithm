#리프 노드의 개수 구하기 
"""
n: 노드 개수 (노드 0부터 시작)
tree: 트리 초기화 
for 노드개수:
    i와 부모 정보를 트리에 양방향으로 저장 

d: 삭제노드 
visited 방문 여부 리스트 

dfs(num)
    리프노드 전역변수 
    자식노드 개수=0
    num 방문여부 표시 
        만약 다음 노드가 방문하지 않았고 삭제노드가 아니면  
            자식노드 개수 +1 
            dfs(다음노드)
    만약 자식노드 개수 0이면 
        리프노드 +1 
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
visited = [False for _ in range(n)]
a = list(map(int,input().split()))
answer = 0 #리프노드 개수 

for i,n in enumerate(a):
    if i != 0:    
        tree[i].append(n)
        tree[n].append(i)
    else:
        root = i

def DFS(num):
    global answer 
    cnode = 0 #자식 노드 개수 
    visited[num] = True
    for next in tree[num]:
        if not visited[next] and next != d_node:
            cnode += 1
            DFS(next) 
    if cnode == 0:
        answer += 1

d_node = int(input())

DFS(root) 

print(answer)