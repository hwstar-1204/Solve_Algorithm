# #n과m(1)

# from itertools import permutations
# n,m = map(int,input().split())
# n_list = [i for i in range(1,n+1)]

# for perm in permutations(n_list, m):
#     print(*perm)

# import sys
# sys.setrecursionlimit(10**6)
def DFS(start):
    for i in range(start,n+1):
        if len(answer) == m:
            print(" ".join(map(str,answer)))
            break
        answer.append(i)
        DFS(i)
        answer.pop()

n,m = map(int,input().split())
answer = []
DFS(1)

    






