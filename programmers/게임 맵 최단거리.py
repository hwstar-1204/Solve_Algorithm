from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])

    def bfs(maps, start_col, start_row):
        nonlocal n, m

        q = deque([(start_col, start_row)])
        visited = [[0] * m for _ in range(n)]
        visited[start_col][start_row] = 1
        
        mx, my = (1,0,-1,0), (0,1,0,-1)
        
        while q:
            col, row = q.popleft()
            
            for x,y in zip(mx, my):
                next_col, next_row = col+x, row+y    
                if 0 <= next_col < n and 0 <= next_row < m:
                    if not visited[next_col][next_row] and maps[next_col][next_row]:
                        q.append((next_col, next_row))
                        visited[next_col][next_row] = visited[col][row] + 1

        return visited[start_col-1][start_row-1]        
    
    ans = bfs(maps, 0, 0)
    return ans if ans else -1

