#칵테일 만들기
"""
N: 재료의 개수 
a: 인접 리스트 
visited: DFS를 탐색할 때 탐색 여부 저장 리스트 
d: 각 노드값 저장 리스트 
lcm: 최소 공배수 

#최대 공약수 gcd()
gcd(a,b):
    if b == 0:
        return a
    else:
        return (b,a%b)

#탐색 함수 구현
DFS:
    visited 리스트에 현재 노드 방문 기록 
    if 현재 노드의 연결 노드 중 방문하지 않은 노드:
        다음 노드의 값 = 현재 노드의 값 * 비율로 저장 
        DFS(다음노드)

for 에지 개수:
    인접 리스트에 이 에지 정보를 저장 
    최소 공배수 업데이트 

0번 노드에 최소 공배수 저장 
0번에서 DFS 탐색 수행
DFS를 이용해 업데이트 된 d 리스트의 값들의 최대 공약수 계산
d 리스트의 각 값을 최대 공약수로 나눠 정답 출력 
"""

n = int(input())
A = [[] for _ in range(n)]
visited = [False] * n
d = [0] * n
lcm = 1 #최소 공배수 

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            d[next] = d[v] * i[2] // i[1]
            DFS(next)

for i in range(n-1):
    a,b,p,q = map(int,input().split())
    A[a].append((b,p,q))
    A[b].append((a,p,q))
    lcm *= (p*q // gcd(p,q))

d[0] = lcm
DFS(0)
mgcd = d[0]

for i in range(1,n):
    mgcd = gcd(mgcd,d[i])

for i in range(n):
    print(int(d[i] // mgcd), end='')