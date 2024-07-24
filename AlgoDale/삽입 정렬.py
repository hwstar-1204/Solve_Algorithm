# 삽입 정렬  
"""
반복1 : 정렬 범위 증가 
반복2 : 범위 내에서 거꾸로 비교 swap 
특징 
1. 정렬 범위를 1칸씩 확장하면서 새롭게 정렬범위에 들어온 값들을 기존 값들과 비교하여 알맞은 곳에 삽입하는 방법 
2. 정렬 범위가 점점 늘어난다. (선택,버블 정렬과 반대)
"""

def insert_sort(arr):
    for end in range(1, len(arr)):
        for j in range(end,0,-1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

a = [2, 1, 5, 4, 3]

# insert_sort(a)
# print(a)

# 최적화 : 여러번의 swap을 피하고 새로운 값이 들어갈 자리를 shift으로 밀어낸 후  삽입 
def insert_sort2(arr):
    for end in range(1,len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i-1] > to_insert:
            arr[i] = arr[i-1]
            i -= 1
        arr[i] = to_insert

insert_sort2(a)
print(a)

