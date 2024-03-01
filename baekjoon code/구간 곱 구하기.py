#구간 곱 구하기 
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
treeheight = 0
length = n
MOD = 1000000007

while length != 0:
    length //= 2
    treeheight += 1

treesize = pow(2,treeheight+1)
tree = [1] * (treesize+1)
leftNodeStartIndex = treesize // 2 - 1

#숫자 배열에 넣어주기 
for i in range(leftNodeStartIndex+1,leftNodeStartIndex+n+1):
    tree[i] = int(input())

#인덱스 트리 만들기 
def setTree(i):
    while i != 1:
        tree[i//2] *= tree[i] %MOD
        i -= 1

setTree(treesize-1)

def changeVal(index,value):
    tree[index] = value
    while index > 1:
        index = index // 2
        tree[index] = tree[index*2] % MOD * tree[index*2+1] % MOD #MOD 숫자 넘지 않게 조절, 부모노드 기준 자식노드의 값으로 부모노드 업데이트 

#구간 곱 연산
def getMul(s,e):
    partMul = 1
    while s <= e:
        if s % 2 == 1:
            partMul *= tree[s] %MOD
            s += 1
        if e % 2 == 0:
            partMul *= tree[e] %MOD
            e -= 1
        s //= 2
        e //= 2
    return partMul 

for _ in range(m+k):
    q,s,e = map(int,input().split())
    if q == 1:
        changeVal(leftNodeStartIndex+s,e)
    elif q == 2:
        s += leftNodeStartIndex
        e += leftNodeStartIndex
        print(getMul(s,e))