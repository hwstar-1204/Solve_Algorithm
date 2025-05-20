"""
주변 살아있는 세포 개수 
살아있는 세포가 주변에 살아있는 세포가 2개 미만 : 죽음 0
살아있는 세포가 주변에 살아있는 세포가 2~3개 : 살아남음 1
살아있는 세포가 주변에 살아있는 세포가 3개 이상 : 죽음 0
죽은세포가     주변에 살아있는 세포가 정확히 3개 : 살아남 1
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                cell = board[i][j]
                lives = self.count_live_cell(board, i, j)

                if cell and (lives < 2 or lives > 3):
                    board[i][j] = -1
                elif (not cell) and lives == 3:
                    board[i][j] = 2

        
        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
        for b in board:
            print(b)
        
        

    def count_live_cell(self, board, x, y):
        dx, dy = (1,1,1,0,-1,-1,-1,0), (-1,0,1,1,1,0,-1,-1)
        cnt = 0
        for tx, ty in zip(dx, dy):
            next_x, next_y = x + tx, y + ty
            if 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
                if abs(board[next_x][next_y]) == 1:
                    cnt += 1
        return cnt
