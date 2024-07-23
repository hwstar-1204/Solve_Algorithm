from collections import deque

class Node:
    def __init__(self, info, num, left=None,  right=None):
        self.info = info
        self.num = num
        self.left = left
        self.right = right
    
    def has_left(self):
        return self.left is not None
    
    def has_right(self):
        return self.right is not None
    
def make_BT(nodeinfo):
    # for i in range(len(nodeinfo)):
    #     nodeinfo[i].append(i+1)
    # sorted_node = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    nodes = [i for i in range(1, len(nodeinfo)+1)]
    nodes.sort(key=lambda x: (-nodeinfo[x-1][1], nodeinfo[x-1][0]))  # 이진트리 번호 레벨순 정렬
    
    root = None
    for i in range(len(nodes)):
        if root is None:
            root = Node(nodeinfo[nodes[0]-1], nodes[0])
        else:
            parent = root
            node = Node(nodeinfo[nodes[i]-1], nodes[i])
            
            while True:
                if node.info[0] < parent.info[0]:  # left
                    if parent.has_left():
                        parent = parent.left
                        continue
                    parent.left = node
                    break
                
                else:  # right
                    if parent.has_right():
                        parent = parent.right
                        continue
                    parent.right = node
                    break 
    return root

def preorder(root, answer):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        answer[0].append(node.num)
        stack.append(node.right)
        stack.append(node.left)
    
def postorder(root, answer):
    stack = [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node is None:
            continue
        if visited:
            answer[1].append(node.num)
        else:    
            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

def solution(nodeinfo):
    answer = [[],[]]
    root = make_BT(nodeinfo)
    preorder(root, answer)
    postorder(root,answer)
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	
print(solution(nodeinfo))