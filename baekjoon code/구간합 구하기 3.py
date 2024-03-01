#구간합 구하기 3
"""
n: 수의 개수, m:변경이 일어나는 개수, k: 구간 합을 구하는 개수 
treeheight : 트리 높이 
length : 리프노드 개수 

트리높이 구하기 #리프 노드의 개수를 2씩 나누어가면서 높이 계산
treesize 구하기 : math.pow(2, 트리의 높이+1)
leftNodeStartIndex 구하기 -> treesize-1 #리프 노드 시작 인덱스 
tree: 인덱스 트리 저장 리스트 

tree 리스트의 리프 노드 영역에 데이터 입력 

#인덱스 트리 생성 함수 
setTree(인덱스):
    while 인덱스가 루트가 아닐때까지:
        부모 노드(인덱스/2)에 현재 index의 트리값 더하기 
        인덱스 1 감소 

setTree(트리의 크기) 함수 호출 #초기 트리 형성 

#값 변경 함수 
changeVal(시작인덱스 변경값):
    diff: 현재 노드이 값과 변경된 값의 차이 
    while 시작 인덱스가 0보다 크다:
        시작 인덱스의 트리값에 diff값 더함 
        시작 인덱스 /= 2

#구간 합 계산 함수 
getSum(시작 인덱스, 종료 인덱스):
    while 시작 인덱스와 종료 인덱스가 교차될 때까지:
        if 시작 인덱스 % 2 == 0:
            해당 노드의 값을 구간 합에 추가 
            시작 인덱스 증가
        if 종료 인덱스 % 2 == 1:
            해당 노드의 값을 구간 합에 추가 
            종료 인덱스 감소 
        시작 인덱스 = 시작 인덱스 / 2
        종료 인덱스 = 종료 인덱스 /2 
    return 구간 합 결과

for m+k만큼 반복:
    question(질의 유형), s(시작인덱스), e(변경값 또는 종료 인덱스)
    #데이터 변경 함수 
    질의가 1일때 -> changeVal(tree에서 시작 인덱스, e)
    #구간합 함수 및 출력 
    질의가 2일떄 -> getSum(tree에서 시작 인덱스, tree에서 종료 인덱스)
"""
import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
treeheight = 0
length = n

while length != 0:
    length //= 2
    treeheight += 1

treesize = pow(2, treeheight+1)
leftNodeStartIndex = treesize // 2 - 1
tree = [0] * (treesize+1)

#데이터를 리프 노드에 저장 
for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i] = int(input())

#인덱스 트리 생성 함수 
def setTree(i):
    while i != 1:
        tree[i//2] += tree[i]
        i -= 1

setTree(treesize-1)

#값 변경 함수 
def changeVal(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] = tree[index] + diff
        index = index // 2

#구간 합 계산 함수 
def getSum(s,e):
    partSum = 0
    while s<= e:
        if s % 2 == 1:
            partSum += tree[s]
            s += 1
        if e % 2 == 0:
            partSum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return partSum

for _ in range(m+k):
    q,s,e = map(int,input().split())
    if q == 1:
        changeVal(leftNodeStartIndex+s,e)
    elif q == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s,e))
        