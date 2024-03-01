#버블 정렬 프로그램1
"""
n: 데이터 개수
a: 데이터 리스트 

for n만큼 반복:
    a리스트 저장 

a 리스트 정렬

for n만큼 반복:
    a[i]의 정렬 전 index - 정렬 후 index 계산의 최댓값을 찾아 저장 

최댓값 _1 을 정답으로 출력
"""

import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()),i))

max = 0
sorted_a = sorted(a)

for i in range(n):
    if max < sorted_a[i][1] - i:
        max = sorted_a[i][1] - i
print(max+1)


# a.sort() : 원래 a리스트를 정렬하여 업데이트하고 반환하지 않는다. (원본 리스트 정렬)
# sorted(a) : a리스트를 정렬하여 새로운 리스트를 생성하고 반환한다. 원래의 리스트는 변경되지않음 (정렬된 새로운 리스트)