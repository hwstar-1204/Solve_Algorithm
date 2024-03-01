#최솟값 찾기2
import sys
input = sys.stdin.readline
n,m = map(int,input().split()) #수의 개수, 범위 개수 
treeheight = 0
length = n

while length != 0:
    length //= 2
    treeheight += 1

treesize = pow(2,treeheight+1)
tree = [sys.maxsize] * (treesize+1)
leftNodeStartIndex = treesize //2 - 1

#데이터를 리프 노드에 저장 
for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i] = int(input())

#인덱스 트리 생성 함수 
def setTree(i):
    while i != 1:
        if tree[i//2] > tree[i]:
            tree[i//2] = tree[i]
        i -= 1


setTree(treesize-1)

#구간 비교 함수 
def getMin(s,e):
    Min = sys.maxsize
    while s<=e:
        if s % 2 == 1:
            Min = min(Min,tree[s])
            s += 1
        if e % 2 == 0:
            Min = min(Min,tree[e])
            e -= 1
        s = s//2
        e = e//2
    return Min 

for _ in range(m):
    s,e = map(int,input().split())
    s = s+leftNodeStartIndex
    e = e+leftNodeStartIndex
    print(getMin(s,e))