"""
n: 재료 개수, m: 갑옷이 되는 번호 
A: 재료 데이터 저장 리스트 
A 리스트 오름차순 정렬 
i : 시작 인덱스 =1
j : 마지막 인덱스 = N-1
count : 정답값 = 0

while i < j:
    if 재료의 합 < M : 작은 번호 인덱스 증가 
    if 재료의 합 > M : 큰 번호 인덱스 감소 
    else: count증가, 양쪽 인덱스 각각 변경 
count 출력 
"""

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
i = 1
j = n-1
count = 0

while i < j:
    if A[i]+A[j] < m:
        i += 1
    elif A[i]+A[j] > m:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)
