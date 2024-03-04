#로프 
import sys
input = sys.stdin.readline

n = int(input())
k_list = [ int(input()) for _ in range(n)]
answer = 0

k_list.sort()

for k in k_list:
    if answer < (k * n):
        answer = k * n
    n -= 1

print(answer)