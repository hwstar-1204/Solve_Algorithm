#다리 놓기 

"""
서쪽 사이트를 다써야함 
m개중에 n개를 골라야하는데 
다리가 겹치면 안된다. == 다리 번호는 오름차순 == 순서가 정해져있음 
어떤 다리를 뽑아도 순서는 정해짐 몇번 다리를 뽑았냐가 중요한것 

"""
# import sys
# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     n,m = map(int,input().split()) #서쪽,<= 동쪽
#     a = [[0]*(m+1) for _ in range(m+1)]

#     for i in range(m+1):
#         a[i][0] = 1
#         a[i][1] = i
#         a[i][i] = 1

#     for i in range(1,m+1):
#         for j in range(1,m+1):
#             a[i][j] = a[i-1][j-1] + a[i-1][j]

#     print(a[m][n])

#---------------------------------
#펙토리얼사용해서 풀기 
from math import factorial

def get_comb(k,n):
    result = (factorial(n)) // (factorial(n-k) * factorial(k))
    return result

n = int(input())

for _ in range(n):
    k,n = map(int,input().split())
    print(get_comb(k,n))
        