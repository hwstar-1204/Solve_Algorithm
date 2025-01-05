from collections import defaultdict
from typing import List

# ver1 - 155ms
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_dict = {}
        col_dict = {}
        ans = 0
        for i in range(len(grid)):
            row_dict[i] = grid[i]
            col_dict[i] = [grid[j][i] for j in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if row_dict[i] == col_dict[j]:
                    ans += 1

        return ans


# ver2 - 47ms
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        int_dict = defaultdict(int)        
        ans = 0

        for row in grid:
            int_dict[str(row)] += 1

        for i in range(len(grid)):
            col = [grid[j][i] for j in range(len(grid))]
            ans += int_dict[str(col)]

        return ans
    
