#소수 구하기 
"""
에라토스테네스의 채 원리 
1. 구하고자 하는 소수의 범위만큼 1차원 리스트를 생성한다. 
2. 2부터 시작하고 현재 숫자가 지워진 상태가 아닌 경우 현재 선택된 숫자의 배수에 해당하는 수를 
리스트에서 끝까지 탐색하면서 지운다. 이때 처음으로 선택된 숫자는 지우지 않는다. 
3. 리스트의 끝까지 2를 반복한 후 리스트에서 남아있는 모든 수를 출력한다. 

m: 시작수 
n: 종료수
a: 소수 리스트 

for n만큼 반복:
    a리스트 초기화 #각각의 인덱스 값으로 

for n의 제곱근까지 반복:
    소수 아니면 넘어감 
    for 소수의 배수 값을 n까지 반복:
        현재 수가 소수가 아니라는것을 표시 

for n~m 까지 반복:
    a에서 소수인 값 출력
"""

import math
m,n = map(int,input().split())
a = [0] * (n+1)

for i in range(2,n+1):
    a[i] = i

for i in range(2,int(math.sqrt(n)+1)):
    if a[i] == 0:
        continue
    for j in range(i+i,n+1,i):
        a[j] = 0

for i in range(m,n+1):
    if a[i] != 0:
        print(a[i])
