# 나이순 정렬
import sys
input = sys.stdin.readline
n = int(input())
n_list = []
for _ in range(n):
    a,b = input().split()
    n_list.append((int(a),b))

n_list.sort(key=lambda x: x[0])
for a in n_list:
    print(*a)