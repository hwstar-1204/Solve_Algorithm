from collections import deque
from typing import List


class Solution1:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        rows, cols = len(maze), len(maze[0])
        row, col = entrance

        visited = [[0] * cols for _ in range(rows)]
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == '+':
                    visited[i][j] = float("inf")
        
        q = deque([[row, col]])
        visited[row][col] = 1

        while q:
            now_row, now_col = q.popleft()

            if (now_row in [0, rows-1] or now_col in [0, cols-1]) and (now_row != row or now_col != col):
                result = visited[now_row][now_col] - 1
                return result if result else -1

            for dx, dy in directions:
                next_row, next_col = now_row + dx, now_col + dy
                if 0 <= next_row < rows and 0 <= next_col < cols and not visited[next_row][next_col] :
                    q.append([next_row, next_col])
                    visited[next_row][next_col] = visited[now_row][now_col] + 1

        return -1


class Solution2:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        rows, cols = len(maze), len(maze[0])
        row, col = entrance
        
        q = deque([[row, col, 0]])
        maze[row][col] = "+"

        while q:
            now_row, now_col, length = q.popleft()

            if (now_row in [0, rows-1] or now_col in [0, cols-1]) and (now_row != row or now_col != col):
                return length

            for dx, dy in directions:
                next_row, next_col = now_row + dx, now_col + dy
                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == ".":
                    maze[next_row][next_col] = "+"
                    q.append([next_row, next_col, length+1])

        return -1

