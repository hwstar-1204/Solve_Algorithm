from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(grid), len(grid[0])
        minutes = 0
        q = deque([])

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 2:
                    q.append([x,y])

        while q:
            now_x, now_y = q.popleft()

            for dx,dy in directions:
                next_x, next_y = now_x + dx, now_y + dy
                if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                    q.append([next_x, next_y])
                    grid[next_x][next_y] = grid[now_x][now_y] + 1

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
            minutes = max(minutes, max(grid[x]))

        return minutes - 2 if minutes else 0