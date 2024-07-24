# 선택정렬
"""
반복1 : 모든 인덱스에 접근
반복2 : 두 값을 비교 후 swap 
시간복잡도 : O(n^2)

특정 
1. 맨 앞부터 정렬해 나아가는데 뒤로 갈수록 비교횟수가 적어짐
2. 어느정도 정렬된 상태와 무관하게 동일한 연산량 
"""
a = [3, 4, 5, 1, 2]
def select_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

select_sort(a)
print(a)