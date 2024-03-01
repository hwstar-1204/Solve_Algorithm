#팩토리얼2
import sys
sys.setrecursionlimit(10**6)
n = int(input())
def pactorial(n):
    if n == 0 or n == 1:
        return 1
    return n * pactorial(n-1)
print(pactorial(n))