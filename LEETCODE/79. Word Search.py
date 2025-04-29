from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board, self.word = board, word
        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0] and self.dfs(i, j, 0):  return True
        return False
    
    def dfs(self, curr_x, curr_y, start_idx):
        if start_idx == len(self.word):  return True
        if not (0 <= curr_x < self.m and 0 <= curr_y < self.n):  return False
        if self.board[curr_x][curr_y] != self.word[start_idx]:  return False
        
        tmp = self.board[curr_x][curr_y]
        self.board[curr_x][curr_y] = "|VISITED|"

        for dx, dy in zip([1,0,-1,0], [0,1,0,-1]):
            if self.dfs(curr_x+dx, curr_y+dy, start_idx+1): return True

        self.board[curr_x][curr_y] = tmp
        return False
