import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y, graph, visited):
    if not graph[x][y] or visited[x][y]:
        return False
    
    visited[x][y] = 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
            dfs(nx, ny, graph, visited)
    return True

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    count = 0

    for _ in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j, graph, visited)
                count += 1
    print(count)


#########################################################

from collections import deque
def bfs(x, y, graph, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1

    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        nx, ny = queue.popleft()
        for i in range(4):
            mx, my = nx+dx[i], ny+dy[i]
            if 0 <= mx < len(graph) and 0 <= my < len(graph[0]):
                if not visited[mx][my] and graph[mx][my]:
                    visited[mx][my] = 1
                    queue.append((mx, my))

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*N for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    count = 0

    for _ in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j, graph, visited)
                count += 1
    print(count)