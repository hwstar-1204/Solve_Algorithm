#여행 가자 
"""
n,m : 도시의 수, 여행계획 도시 수 
n*n 행렬 : 도시들 간의 연결정보 인접행렬 
여행계획 
(도시번호는 1번부터 n번까지)

유니온 파인드 
인접행렬구조를 에지 리스트로 변환
모든 에지를 돌면서 대표노드 리스트 업데이트 

처음 출발도시의 집합과 도착도시의 집합이 같은지 확인 
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)

n = int(input())
m = int(input())
dosi = [list(map(int,input().split())) for _ in range(n)] #인접 행렬
myTravel = list(map(int,input().split()))
parent = [i for i in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

def checkGroup(a,b):
    a = find(a)
    b = find(b)
    return True if a==b else False

# dosi_list = [] #에지 리스트 
for i in range(n):
    for j in range(i,n):
        if dosi[i][j] == 1:
            # start = i+1
            # end = j+1
            union(i+1,j+1)
            # dosi_list.append((start,end))

# for s,e in dosi_list: #도시 연결 
#     union(s,e) 

for k in range(len(myTravel)-1):
    now = find(myTravel[k])
    next = find(myTravel[k+1])
    if now != next:
        print("NO")
        break
else:
    print("YES")