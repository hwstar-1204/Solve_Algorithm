# 퀵 정렬 
"""
특징
1. pivot 값의 선택에 따라 시간복잡도가 달라짐 => 보통 중간값
2. 원소의 개수가 적을수록 나쁜 중간값이 선택될 수 있음 
3. 합병정렬과의 차이점은 분할 시점에서 비교연산이 이루어진다. 
시간 복잡도
최악 : n^2
최선 : nlogn
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [], []
    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)


a = [15,6,45,4,3,5,3,2,1]
print(quick_sort(a))


# 최적화 (슬라이싱 사용하지 않고 in-place으로 메모리 사용 줄임)
def quick_sort1(arr):
    def sort(low,high):
        if high <= low:
            return 
        
        mid = partition(low,high)
        sort(low,mid)
        sort(mid,high)

    def partition(low,high):
        pivot = arr[(low + high)//2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low +1, high -1
        return low 
    
    return sort(0,len(arr)-1)
