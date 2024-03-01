#신기한 소수 찾기 
"""
n: 자릿수 
#소수를 구하기 위한 함수 
for i를 2~현재 수/2+1까지 반복:
    if 현재 수 % i가 0이면:
        return 소수가 아님 

#DFS 구현 
DFS(숫자):
    if 숫자 == N:
        현재 수 출력 
    else:
        for i를 1~9반복:
            if i를 붙인 새로운 수가 홀수이면서 소수일때 #소수구하기 함수 사용
                DFS(수 * 10 + 뒤에 붙는 수 ) 실행 

DFS 실행 (숫자 2,3,5,7로 탐색 시작)
"""

import sys
import math
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())

#숫자의 절반까지만 탐색
def isPrime(num):
    for i in range(2, int(num/2 +1)): 
        if num % i == 0:
            return False
    return True

# num = 25   i = 2~13
# num이 i로 나눠떨어지면 소수 아님 
# num 28 i = 2~15

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0:
                continue
            if isPrime(number*10 + i):
                DFS(number*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)