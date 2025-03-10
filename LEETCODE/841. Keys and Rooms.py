from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [1] + [0] * (n-1)
        
        stack = [0]
        while stack:
            now = stack.pop()
            visited[now] = 1
            for next in rooms[now]:
                if not visited[next]:
                    stack.append(next)

        if sum(visited) == n:
            return True
        return False 