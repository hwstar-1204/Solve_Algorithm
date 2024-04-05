# 직각삼각형
import sys
input = sys.stdin.readline
while True:
    m = list(map(int, input().split()))
    if sum(m) == 0:
        break
    m.sort()
    if m[2]**2 == (m[0]**2+m[1]**2):
        print('right')
    else:
        print('wrong')