def solution(maps):
    days = [] 
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    
    def dfs(x, y):
        stack = [(x,y)]
        directs = [(1,0), (-1,0), (0,1), (0,-1)]
        total = int(maps[x][y])
        visited[x][y] = True

        while stack:
            curr_x, curr_y = stack.pop()
            for dx, dy in directs:
                nx, ny = curr_x+dx, curr_y+dy
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] != "X" and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                        total += int(maps[nx][ny])
        return total
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                days.append(dfs(i, j))
                
    return sorted(days) if len(days) > 0 else [-1]