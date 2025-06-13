from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_distnace = 0
        x,y,d = 0,0,0

        directs = [(0,1), (1,0), (0,-1), (-1,0)]
        obstacles = set(map(tuple, obstacles))

        for command in commands:
            if command == -1:  # turn right
                d = (d+1) % 4
            elif command == -2:  # turn left
                d = (d-1) % 4
            else:
                for _ in range(command):
                    nx = x + directs[d][0]
                    ny = y + directs[d][1]
                    if (nx,ny) in obstacles:
                        break

                    x,y = nx,ny
                    max_distnace = max(max_distnace, x**2 + y**2)
        return max_distnace
