#내림차순으로 자릿수 정렬하기 
"""
a: 자릿수별로 구분해 저장한 리스트 

for i를 a리스트 만큼 반복:
    for j를 i+1 ~ a리스트 길이만큼 반복:
        현재 범위에서 max찾기
    현재 i의 값과 max값 중 max값이 더 크면 swap진행

a리스트 출력 
"""
import sys
print = sys.stdout.write

a = list(input())

for i in range(len(a)):
    max = i
    for j in range(i+1,len(a)):
        if a[max] < a[j]:
            max = j
    if a[i] < a[max]:
        temp = a[i]
        a[i] = a[max]
        a[max] = temp

for i in range(len(a)):
    print(a[i])