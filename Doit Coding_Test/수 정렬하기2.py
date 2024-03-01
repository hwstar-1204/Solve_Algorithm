#수 정렬하기2
"""
병합정렬 구현
병합정렬(s,e):
    s(시작점),e(종료점),m(중간점)
    #재귀함수 형태로 구현
    병합 정렬(s,e)
    병합 정렬(m+1,e)
    for s~e:
        tmp 리스트 저장 

    #두 그룹을 병합하는 로직
    index1 -> 앞쪽 그룹 시작점
    index2 -> 뒤쪽 그룹 시작점
    while index1 <= 중간점 and index2 <= 종료점:
        양쪽 그룹의 index가 가리키는 값을 비교한 후 더 작은수를 선택해 리스트에 저장하고 
        선택된 데이터의 index값을 오른쪽으로 한칸 이동
        반복문이 끝난 후 남아있는 데이터 정리 

n: 정렬할 수 개수 
a: 정렬할 리스트 선언 
tmp: 정렬할 때 잠시 사용할 임시 리스트 선언

for n개수 만큼:
    a리스트에 데이터 더하기 

병합 정렬 함수 수행 
결괏값 출력 
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(s,e):
    if e-s < 1: return #한개 있을떄 
    m = int(s+(e-s)/2)  #중간점 계산 
    merge_sort(s,m)
    merge_sort(m+1,e)
    
    for i in range(s,e+1):
        tmp[i] = a[i]
    
    k = s
    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e: #두 그룹을 병합하는 로직 
        if tmp[index1] > tmp[index2]:
            a[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            a[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        a[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= m:
        a[k] = tmp[index2]
        k += 1
        index2 += 1
        




n = int(input())
a = [0] * int(n+1)
tmp = [0] * int(n+1)

for i in range(1,n+1):
    a[i] = int(input())

merge_sort(1,n)

for i in range(1,n+1):
    print(str(a[i]) + '\n')