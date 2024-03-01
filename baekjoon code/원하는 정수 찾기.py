#원하는 정수 찾기 
"""
n: 수 개수 저장 
a: 수 데이터 리스트 저장 
a 리스트 정렬
m: 탐색할 숫자 개수 
target_list: 탐색할 수 데이터 리스트 저장 

for m 개수만큼 반복:
    target: 찾아야하는 수 
    start: 시작 인덱스
    end: 끝 인덱스 
    while 시작 인덱스 < 끝 인덱스:
        midi: 중간 인덱스 
        midv: 중앙값
        if 중앙값 > target:
            end = mid - 1
        if 중앙값 < target:
            start = mid + 1
        else:
            찾음 , 반복문 종료 

    if 찾았음:
        1출력
    else:
        0출력

"""

n = int(input()) #리스트 숫자 개수
a = list(map(int,input().split()))
m = int(input()) #찾아야할 숫자 개수 
target_list = list(map(int,input().split()))

a.sort()

for i in range(m):
    find = False
    target = target_list[i]
    start = 0
    end = len(a) - 1
    while start <= end:
        midi = (start+end)//2
        midv = a[midi]
        if midv > target:
            end = midi-1
        elif midv < target:
            start = midi+1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)