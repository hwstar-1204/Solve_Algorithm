# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None

            if not root.left or not root.right:
                return root.left or root.right

            root.val = self.findMin(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root


    def findMin(self, node: Optional[TreeNode]) -> int:
        min_val = node.val
        while node.left:
            min_val = node.left.val
            node = node.left
        return min_val
