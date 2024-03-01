#여행 계획 짜기 
"""

"""

n = int(input()) #도시 개수
m = int(input()) #경로 개수 
dosi = [[0 for j in range(n+1)] for i in range(n+1) ]

parent = [0]*(n+1)

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

#도시 연결 데이터 저장 
for i in range(1,n+1):
    dosi[i] = list(map(int,input().split()))
    dosi[i].insert(0,0) #도시는 1부터 시작함으로 앞에 추가 

#여행 도시 정보 저장 
route = list(map(int,input().split()))
route.insert(0,0)

for i in range(1,n+1):
    for j in range(1,n+1):
        if dosi[i][j] == 1:
            union(i,j)

index = find(route[1])
isConect = True

for i in range(2,len(route)):
    if index != find(route[i]):
        isConect = False
        break

print("YES" if isConect else "NO")