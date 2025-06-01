import heapq
from collections import deque
from typing import List


class Solution:
    
    #------------------------ BFS ------------------------#
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        return self.bfs(board, n)
        
    def bfs(self, board, n):
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            pos, moves = queue.popleft()
            if pos == n * n:
                return moves
            for next_pos in range(pos + 1, min(pos + 7, n * n + 1)):
                row, col = self.get_place(n, next_pos)
                dest = board[row][col] if board[row][col] != -1 else next_pos
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        return -1

    def get_place(self, n: int, s: int) -> tuple[int, int]:
        quot, rem = divmod(s - 1, n)
        row = n - 1 - quot
        if quot % 2 == 0:
            col = rem
        else:
            col = n - 1 - rem
        return row, col
    
    #------------------------ 다익스트라 ------------------------#
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        pq = [(0,1)]  # distance, start
        distance = [float("inf")] * (n * n + 1)

        while pq:
            moves, pos = heapq.heappop(pq)
            if pos == n * n:
                return moves
            
            for next_pos in range(pos + 1, min(pos+7, n*n+1)):
                if moves + 1 < distance[next_pos]:
                    distance[next_pos] = moves + 1
                    row, col = self.get_place(next_pos)
                    dest = board[row][col] if board[row][col] != -1 else next_pos
                    heapq.heappush(pq, (moves + 1, dest))

        return -1
