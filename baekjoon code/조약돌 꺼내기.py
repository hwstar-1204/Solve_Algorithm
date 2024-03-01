#조약돌 꺼내기 
"""
n개의 조약돌 중 k개를 뽑았을때 모두 같은 색일경우 

# H(m,k) = C(m+k-1,k) / 돌 전체 개수 

18c2 = 17*9 = 153
5c2+6c2+7c2 = 10+15+21 = 46
"""

# import sys
# from math import factorial
# input=sys.stdin.readline
# m = int(input()) #색상 종류
# doll = list(map(int,input().split()))
# k = int(input()) #뽑는 개수

# def comb(m,k):
#     return factorial(m) / (factorial(m-k) * factorial(k))

# doll_comb_sum = 0
# for n in doll:
#     doll_comb_sum += comb(n,k)
# total_comb = comb(sum(doll),k)

# print(doll_comb_sum / total_comb)




import sys
import math
input=sys.stdin.readline
m = int(input()) #색상 종류
doll = list(map(int,input().split()))
k = int(input()) #뽑는 개수
doll_comb_sum = 0
for n in doll:
    doll_comb_sum += math.comb(n,k)
total_comb = math.comb(sum(doll),k)

print(doll_comb_sum / total_comb)