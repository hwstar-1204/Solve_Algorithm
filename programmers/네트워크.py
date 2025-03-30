"""
각 지점에서 DFS 순회
방문 노드 표시 
한번 순회할때마다 networks += 1
"""

# 스택
def DFS(computers, visited, now):
    stack = [now]
    visited[now] = True

    while stack:
        now = stack.pop()
        for i, connected in enumerate(computers[now]):
            if connected and not visited[i]:
                visited[i] = True
                stack.append(i)

def solution(n, computers):
    networks = 0
    visited = [False] * n
            
    for i in range(n):
        if not visited[i]:
            DFS(computers, visited, i)
            networks += 1

    return networks

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #

# 재귀
def DFS(computers, visited, now):
    visited[now] = True
    
    for i in range(n):
        if computers[now][i] and not visited[i] and i != now:
            DFS(n, computers, visited, i)
        

def solution(n, computers):
    networks = 0
    visited = [False] * n
            
    for i in range(n):
        if not visited[i]:
            DFS(computers, visited, i)
            networks += 1
    
    return networks

# ------------------------------------------------------------- #
# ------------------------------------------------------------- #

# 스택 list -> deque
from collections import deque

def DFS(computers, visited, now):
    stack = deque([now])
    visited[now] = True

    while stack:
        now = stack.pop()
        for i, connected in enumerate(computers[now]):
            if connected and not visited[i]:
                visited[i] = True
                stack.append(i)

def solution(n, computers):
    networks = 0
    visited = [False] * n
            
    for i in range(n):
        print(visited)
        if not visited[i]:
            DFS(computers, visited, i)
            networks += 1

    return networks

