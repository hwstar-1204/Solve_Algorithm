"""
{
    a: {b:2}
    b: {a: 1/2}, {c: 3}
    c: {b: 1/3}
}
"""
from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(
        self,
        equations: List[List[str]], 
        values: List[float], 
        queries: List[List[str]]
    ) -> List[float]:

        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        ans = []
        for c, d in queries:
            if c not in graph or d not in graph:
                ans.append(-1)
                continue

            visited = set()
            result = self.dfs(graph, visited, c, d, 1.0)
            ans.append(result if result is not None else -1)

        return ans

    def dfs(self, graph: dict[str, dict[str, float]], visited: set, now, end, value):
        if now == end:
            return value
        
        visited.add(now)

        for next_node, weight in graph[now].items():
            if next_node not in visited:
                result = self.dfs(graph, visited, next_node, end, value * weight)
                if result is not None:
                    return result
        return None