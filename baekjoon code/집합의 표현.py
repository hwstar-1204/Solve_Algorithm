#집합의 표현 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split()) #n개의 집합, 연산개수 
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
    # if a != b:
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b 

for _ in range(m):
    op,a,b = map(int,input().split())

    if op == 0:
        union(a,b)#유니온
    else:
        print("YES") if find(a)==find(b) else print("NO")   #파인드 