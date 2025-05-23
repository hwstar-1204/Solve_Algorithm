from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 첫 번째 풀이 : 중위 순회
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
  
        prev = None
        start_node = None
        last_node = None
        
        def dfs(root: Optional[TreeNode]):
            nonlocal prev, start_node, last_node
            if not root:  return
            
            dfs(root.left)

            if prev and prev.val > root.val:
                if not start_node:
                    start_node = prev
                last_node = root

            prev = root
            
            dfs(root.right)
        
        dfs(root)

        if start_node and last_node:
            start_node.val, last_node.val = last_node.val, start_node.val

    # 두 번째 풀이 : 전위 순회
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = None
        
        def find_wrong_node(node, min_node, max_node):
            nonlocal first, second
            
            if not node:
                return
            
            if min_node and node.val < min_node.val:
                if not first:
                    first = min_node
                second = node
            if max_node and node.val > max_node.val:
                if not first:
                    first = node
                second = max_node
            
            find_wrong_node(node.left, min_node, node)
            find_wrong_node(node.right, node, max_node)
        
        find_wrong_node(root, None, None)
        
        if first and second:
            first.val, second.val = second.val, first.val