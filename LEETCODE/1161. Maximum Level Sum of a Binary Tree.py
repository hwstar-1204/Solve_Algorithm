from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        smallest_lv = 1
        now_lv = 1
        max_sum = root.val
        queue = deque([root])

        while queue:
            n = len(queue)
            l_sum = 0
            for i in range(n):
                node = queue.popleft()
                l_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if l_sum > max_sum:
                max_sum = l_sum
                smallest_lv = now_lv

            now_lv += 1

        return smallest_lv
        