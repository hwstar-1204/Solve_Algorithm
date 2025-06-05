from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(set)
        for st1, st2 in zip(s1, s2):
            graph[st1].add(st2)
            graph[st2].add(st1)

        def dfs(st: str, visited: set):
            visited.add(st)
            min_st = st
            for next_st in graph[st]:
                if next_st not in visited:
                    candidates = dfs(next_st, visited)
                    min_st = min(min_st, candidates)
            return min_st
        
        results = []
        for st in baseStr:
            visited = set()
            results.append(dfs(st, visited))

        return ''.join(results)
