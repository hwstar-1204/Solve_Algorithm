#알바생 강호
import sys
input = sys.stdin.readline

n = int(input())
customer = [int(input()) for _ in range(n)]
answer = 0

customer.sort(reverse=True)

for i,c in enumerate(customer,1):
    tip = c - (i-1) 
    answer += tip if tip > 0 else 0

print(answer)