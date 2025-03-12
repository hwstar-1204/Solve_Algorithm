from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)
    
        n = len(isConnected)
        visited = [False for _ in range(n)]
        groups = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                groups += 1
                dfs(i)
        return groups
