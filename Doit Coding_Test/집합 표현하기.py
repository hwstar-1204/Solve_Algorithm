#집합 표현하기 
"""
n: 원소 개수
m: 질의 개수 
parent: 대표 노드 저장 리스트 

#find
find(a):
    a가 대표노드이면 return 
    아니면 a의 대표 노드값을 find(parent[a]) 값으로 저장 -> 재귀 함수 형태 

#union
union(a,b):
    a와 b의 대표노드 찾기 
    두 원소의 대표 노드끼리 연결 

#checksame
checksame(a,b):
    a와 b의 대표노드 찾기 
    두 대표 노드가 같으면 true
    아니면 false return 

for n만큼 반복:
    대표노드를 자신으로 초기화 

for m만큼 반복:
    질의가 0이면:
        유니온
    else:
        같은 집합 원소인지 확인하고 결괏값 출력 
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m = map(int,input().split())
parent = [0] * (n+1)

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

def checksame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False
    
for i in range(n):
    parent[i] = i

for i in range(m):
    question,a,b = map(int,input().split())
    if question == 0:
        union(a,b)
    else:
        if checksame(a,b):
            print("True")
        else:
            print("False")