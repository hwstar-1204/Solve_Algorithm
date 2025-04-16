import heapq

def solution(board):
    n, INF = len(board), int(1e9)
    cost_board = [[INF]*n for _ in range(n)]
    cost_board[0][0] = 0
    
    def bfs(start_x, start_y):
        heap = []
        heapq.heappush(  # x, y, 이전 방향, 누적 비용
            heap, (start_x, start_y, -1, cost_board[start_x][start_y])
        )

        directions = [(-1,0),(0,1),(1,0),(0,-1)]        
        
        while heap:
            x, y, prev_dir, cost = heapq.heappop(heap)

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                    if prev_dir == i or prev_dir == -1:  # 직선 or 초기 방향
                        new_cost = cost + 100
                    else:  # 코너
                        new_cost = cost + 600
                    
                    if cost_board[nx][ny] >= new_cost:
                        cost_board[nx][ny] = new_cost
                        heapq.heappush(heap, (nx, ny, i, new_cost))  # 다음 x, 다음 y, 현재 이동 방향, 최소 누적 비용
    
    bfs(0,0)
    return cost_board[n-1][n-1]
