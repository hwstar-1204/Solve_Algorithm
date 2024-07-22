"""
시작점 S, 레버 L, 출구 E 찾기 
s에서 레버까지 최단거리 
레버에서 출구까지 최단거리 

"""
from collections import deque

def BFS(start, end, maps):
    queue = deque([start])
    length = len(maps)
    visited = [[0] * 5 for _ in range(length)]
    
    mxy = [(1,0), (0,1), (-1,0), (0,-1)]
    
    while queue:
        nx, ny = queue.popleft()

        if (nx,ny) == end:
            return visited[nx][ny]
        
        for mx,my in mxy:
            next_x = nx + mx
            next_y = ny + my
            if 0 <= next_x < 5 and 0 <= next_y < length:
                if not visited[next_x][next_y] and maps[next_x][next_y] != "X":
                    queue.append((next_x, next_y))
                    visited[next_x][next_y] = visited[nx][ny] + 1
    
    return 0

def solution(maps):
    target = dict()
    
    for i in range(len(maps)):
        for j in range(5):
            now = maps[i][j]
            if now == "S":
                target["S"] = (i,j)
            elif now == "L":
                target["L"] = (i,j)
            elif now == "E":
                target["E"] = (i,j)
                
    first = BFS(target["S"], target["L"], maps)
    second = BFS(target["L"], target["E"], maps)
    
    if first and second:
        return first + second
    else:
        return -1
    

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

print(solution(maps))