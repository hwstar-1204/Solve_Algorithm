from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n,m = len(edges1), len(edges2)
        if not k:  return [1 for _ in range(n + 1)]

        tree1 = self.create_tree(edges1)
        tree2 = self.create_tree(edges2)

        tree1_links = [self.bfs(tree1, idx, k) for idx in range(n + 1)]
        tree2_links = [self.bfs(tree2, idx, k-1) for idx in range(m + 1)]

        tree2_top_links = max(tree2_links)

        return [links + tree2_top_links for links in tree1_links]

    
    def create_tree(self, edges: List[List[int]]) -> list[list[int]]:
        tree = [[] for _ in range(len(edges)+1)]

        for e1,e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)

        return tree


    def bfs(self, tree: list[list[int]], start: int, k: int) -> int:
            lvl, links, visited = 0, 1, set([])
            
            q = deque([start])
            visited.add(start)

            while q and lvl < k:
                for _ in range(len(q)):
                    now = q.popleft()
                    for nxt in tree[now]:
                        if nxt not in visited:
                            visited.add(nxt)
                            links += 1
                            q.append(nxt)
                lvl += 1

            return links 
