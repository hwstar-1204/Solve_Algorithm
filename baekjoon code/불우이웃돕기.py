#불우이웃돕기 
"""
n: 컴퓨터의 개수 
랜선의 길이 인접행렬
i==j는 같은컴퓨터 연결이므로 저장 X
a~z = 1~26, A~Z = 27~52
랜선의 길이를 숫자료 변형 

저장된 에지 리스트로 최소신장트리

결괏값: 전체 랜선길이 - 최소신장트리결과
최소신장트리에서 사용한 에지 개수가 n-1이 아닌경우 모든 컴퓨터 연결 불가하므로 -1 
"""

import sys
from queue import PriorityQueue
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()
sum = 0

for i in range(n):  #인접행렬을 에지 리스트로 큐에 넣음 
    tempc = list(input())
    for j in range(len(tempc)):
        temp = 0
        if 'a' <= tempc[j] <= 'z':
            temp = ord(tempc[j])-ord('a')+1
        elif 'A' <= tempc[j] <= 'Z':
            temp = ord(tempc[j])-ord('A')+1
        sum += temp 
        if i != j and temp != 0:
            pq.put((temp,i,j))

parent = [i for i in range(n)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdges = 0
result = 0

while pq.qsize() > 0:
    w,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        useEdges += 1
        result += w 

if useEdges == n-1:
    print(sum-result)
else:
    print(-1)