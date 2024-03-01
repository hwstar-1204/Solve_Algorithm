# 오일러 피 함수 구현하기 
"""
n: 소인수 표현
result: 결괏값

for 2~n의 제곱근:
    if 현재 값이 소인수라면:
        결괏값 = 결괏값 - 결괏값 / 현재 값 
        n에서 현재 소인수 내역을 제거 

if n > 1: #n이 마지막 소인수일때
    결괏값 = 결괏값 - 결괏값 / n

결괏값 출력 
"""
import math
n = int(input())
result = n

for p in range(2,int(math.sqrt(n)) + 1): #제곱근까지만 진행
    if n % p == 0:
        result -= result/p
        while n % p == 0:
            n /= p

if n > 1:
    result -= result/n
print(int(result))