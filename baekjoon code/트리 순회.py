# #트리 순회 
# """
# 전위 ,중위, 후위 순회한 값을 출력 

# n = 이진 트리의 노드 개수 
# tree = 노드개수+1개 크기의 이중 리스트 

# #트리 초기화 
# for _ in range(n):
#     root,left,right = 입력값 
#     tree[root]에 left,right 값 추가 

# def 전위 순회:
#     #root->left->right

#     if root가 '.'이면:
#         return 
#     root 출력 

#     전위순회(left)
#     전위순회(right)
# """

# # class Node(object):
# #     def __init__(self,item):
# #         self.item = item
# #         self.left = self.right = None

# # class BinaryTree(object):
# #     def __init__(self):
# #         self.root = None

# # class Node():
# #     def __init__(self,item,left,right):
# #         self.item = item
# #         self.left = left
# #         self.right = right

n = int(input())
tree = {}

for _ in range(n):
    root, left, right = map(str,input().split())
    tree[root] = [left,right]

def preorder(root):
    if root == '.':
        return
    left, right = tree[root]

    print(root, end='')
    preorder(left)
    preorder(right)

def inorder(root):
    if root == '.':
        return
    left, right = tree[root]
    
    inorder(left)
    print(root, end='')
    inorder(right)

def postorder(root):
    if root == '.':
        return
    left, right = tree[root]
    
    postorder(left)
    postorder(right)
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
