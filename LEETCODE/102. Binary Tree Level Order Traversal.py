from collections import deque, defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict()
        
        def bfs(start : TreeNode):
            q = deque([])
            q.append((start, 0))

            while q:
                now, lvl = q.pop()
                if not now: continue

                if now.left:
                    q.appendleft((now.left, lvl+1))
                if now.right:
                    q.appendleft((now.right, lvl+1))
                
                if lvl in ans.keys():
                    ans[lvl].append(now.val)
                else:
                    ans[lvl] = [now.val]

        bfs(root)
        return [v for k,v in ans.items()]
    