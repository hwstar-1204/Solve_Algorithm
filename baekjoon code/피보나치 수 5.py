#피보나치 수 5
import sys
sys.setrecursionlimit(10**6)
n = int(input())

def pibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return pibonachi(n-2) + pibonachi(n-1)
print(pibonachi(n))