# 버블 정렬 
"""
반복1 : 반복 구간 설정 
반복2 : 반복하면서 앞뒤 비교 후 swap 
시간 복잡도 : O(n^2)

특징
1. 뒤에서부터 앞으로 정렬해 나아가는 방식 (선택 정렬과 반대)
2. 앞뒤 자리를 비교해서 맨뒤로 가장 큰값을 보내는 방식 
3. swap 횟수가 많다. 
"""

a = [3, 4, 5, 1, 2]
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

# bubble_sort(a)
# print(a)

# 최적화 : 이전 반복에서 swap한 변화가 없을경우 정렬이 된 상태이므로 stop

def bubble_sort2(arr):
    for i in range(len(arr)-1, 0, -1):
        swap = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break

# bubble_sort2(a)
# print(a)


# 최적화 : 마지막으로 swap이 이루어진 곳을 기억하고 그 이후는 정렬된 상태로 보고 그 이전 구간만 정렬 
def bubble_sort3(arr):
    end = len(arr) - 1
    while end > 0:
        last_swap_idx = 0
        for i in range(end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last_swap_idx = i
        end = last_swap_idx
        print(*arr)

b = [4,2,3,6,9,1,7]
bubble_sort3(b)
print(b)

"""
[4,2,3,6,9,1,7]
[2,3,4,6,1,7,9]
[2,3,4,1,6,7,9]
[2,3,1,4,6,7,9]
[2,1,3,4,6,7,9]
[1,2,3,4,6,7,9]
"""