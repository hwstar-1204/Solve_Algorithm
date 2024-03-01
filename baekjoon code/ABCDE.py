import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split()) #사람수, 관계수
freinds = [[] for _ in range(n)]
visited = [False for _ in range(n)]
answer = False

for i in range(m):
    f1,f2 = map(int,input().split())
    freinds[f1].append(f2)
    freinds[f2].append(f1) 

def DFS(idx,depth):
    global answer 
    visited[idx] = True
    if depth == 4:
        answer = True
        return 
    
    for next in freinds[idx]:
        if not visited[next]:
            visited[next] = True
            DFS(next,depth+1)
            visited[next] = False

for i in range(n):
    DFS(i,0)
    visited[i] = False
    if answer:
        break
if answer:
    print(1)
else:
    print(0)