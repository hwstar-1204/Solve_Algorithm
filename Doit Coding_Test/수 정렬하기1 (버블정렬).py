#수 정렬하기1 (버블정렬)
"""
n: 수의 개수
arr: 수를 저장할 배열

a: 수 저장 리스트 선언 및 입력 데이터 저장

for i를 0~n-1만큼 반복:
    for j를 0 ~ n-1-i만큼 반복:
        현재 a리스트값보다 1칸 오른쪽 값이 더 작으면 스왑 

리스트 출력
"""
n = int(input())
arr = [0]*n
for i in range(n):
    x = int(input())
    arr[i] = x

for i in range(0,n-1):
    for j in range(0,n-1-i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

for i in range(n):
    print(arr[i])