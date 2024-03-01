#트리 순회하기 
"""
n: 이진트리의 노드 개수 , tree: 트리 데이터 저장 

for n :
    root,left,right 
    tree 딕셔너리에 데이터 저장 

전위순회 :
    if 현재값 == '.':
        retrun 
    1.현재노드 출력 
    2.왼쪽자식노드 출력 
    3.오른쪽자식노드 출력 

중위,후위는 위의 번호 순서만 달리함 
"""

import sys
input = sys.stdin.readline
n = int(input())
tree = {}

for _ in range(n):
    root,left,right = input().split()
    tree[root] = [left,right]

def preOrder(now):
    if now == '.':
        return 
    print(now,end='')
    preOrder(tree[now][0])
    preOrder(tree[now][1])

def inOrder(now):
    if now == '.':
        return 
    inOrder(tree[now][0])
    print(now,end='')
    inOrder(tree[now][1])

def postOrder(now):
    if now == '.':
        return 
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now,end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')