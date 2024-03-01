#k번째 수 구하기 (퀵 정렬)
"""
n: 숫자의 개수 
k: k번째 수 
a: 숫자 데이터 저장 배열 

퀵정렬 함수(시작,종료,k):
    피벗 구하기 함수(시작,종료)
    if 피벗 == k: 종료 
    elif k < 피벗: 퀵 정렬 수행하기 (시작,피벗-1,k) 
    else: 퀵 정렬 수행하기 (피벗+1,종료,k)

피벗 구하기 함수 (시작,종료)
    데이터가 2개인 경우는 바로 비교하여 정렬 
    M: 중앙값
    중앙값을 시작 위치와 swap
    pivot을 시작 위치 값 a[s]로 저장 
    i: 시작점
    j: 종료점

    while i<=j:
    피벗보다 큰 수가 나올떄까지 i증가
    피벗보다 작은 수가 나올떄까지 j감소 
    찾은 i와 j 데이터를 swap

    피벗 데이터를 나뉜 두 그룹의 경계 index에 저장하기 
    경계 Index 리턴 

퀵정렬 실행
k번째 데이터 출력 
"""

import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))

def quickSort(s,e,k):
    global a
    if s < e:
        pivot = partition(s,e)
        if pivot == k:
            return 
        elif k < pivot:
            quickSort(s,pivot-1,k)
        else:
            quickSort(pivot+1,e,k)

def swap(i,j):
    global a
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(s,e):
    global a

    if s+1 == e:
        if a[s] > a[e]:
            swap(s,e)
        return e

    m = (s+e)//2
    swap(s,m)
    pivot = a[s]
    i = s+1
    j = e
    
    while i <= j:
        while pivot < a[j] and j >0:
            j -= 1
        while pivot > a[i] and i < len(a)-1:
            i += 1
        if i <= j:
            swap(i,j)
            i += 1
            j -= 1

    a[s] = a[j]
    a[j] = pivot 
    return j 

quickSort(0,n-1,k-1)
print(a[k-1])