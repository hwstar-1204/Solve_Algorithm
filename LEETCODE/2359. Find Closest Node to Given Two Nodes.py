from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dfs(node: int): 
            distance = 0
            visited = [-1 for _ in range(len(edges))]
            
            while node != -1 and visited[node] == -1:
                visited[node] = distance
                node = edges[node]
                distance += 1
            
            return visited

        ans = -1
        distance = float("inf")
        visited1, visited2 = dfs(node1), dfs(node2)

        for idx, (n1, n2) in enumerate(zip(visited1, visited2)):
            if n1 == -1 or n2 == -1:  continue
            
            if max(n1,n2) < distance:
                distance = max(n1,n2)
                ans = idx

        return ans
