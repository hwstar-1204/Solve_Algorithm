"""
- 0에서 DFS 시작 
- 정방향으로 갈수있는 도시면 ans +1 
- 0에서 어떤 도시로 정방향으로 갈 수 있다는 뜻 == 절대 0으로 갈 수 없는 길 (뒤집어야할 길 += 1)
"""

from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.ans = 0
        
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for connection in connections:
            a,b = connection
            graph[a].append([b, 1])  # 정방향
            graph[b].append([a, -1])  # 역방향 (dfs하기위해 모든 길을 터놓고 시작)
        
        self.dfs(graph, visited, 0)
        return self.ans

    def dfs(self, graph, visited, now: int):
        visited[now] = True
        for next_city, direction in graph[now]:
            if not visited[next_city]:
                if direction == 1:  # 0에서 정방향으로 갈 수 있는 도시 
                    self.ans += 1
                self.dfs(graph, visited, next_city)

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
s = Solution()
ans = s.minReorder(n, connections)
print(ans)