#거짓말쟁이가 되긴싫어
"""
n: 사람 수 
m: 파티 수 
trueP: 진실을 아는 사람 데이터 
T: 진실을 아는 사람 수 
party: 파티 데이터 

find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

checksame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return true
    else:
        return false

파티 데이터 저장

for n만큼 반복:
    대표노드를 자신으로 초기화 

for m만큼 반복:
    firstPeople : i번째 파티의 1번째 사람 
    for j를 i번째 파티의 사람 수 만큼 반복:
        union(firstPeople,j) #각 파티에 참가한 사람들을 1개의 그룹으로 묶음

for m만큼 반복:
    firstPeople (i번째 파티의 첫번째 사람)
    for j -> 진실을 아는 사람 수 만큼 반복:
        find(firstpeople)과 find(trueP[j]) 값 비교 
    모두 다르면 결괏값 1증가 (들키지 않고 과장 가능)

결괏값 출력
"""
n,m = map(int,input().split())
trueP = list(map(int,input().split()))
T = trueP[0]
del trueP[0]
result = 0
party = [[] for _ in range(m)]

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

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False
    
for i in range(m):
    party[i] = list(map(int,input().split()))
    del party[i][0]
    
parent = [0] * (n+1)

for i in range(n):
    parent[i] = i

for i in range(m):
    firstPeople = party[i][0]
    for j in range(1,len(party[i])):
        union(firstPeople,j)

for i in range(m):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(T):
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
        if isPossible:
            result += 1

print(result)
