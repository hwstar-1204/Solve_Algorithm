"""
arr: n개의 양의 정수 리스트
target: 정수

이 중 합이 target인 두 수가 arr에 있는지 찾고 있으면 True 아니면 False 
"""

def two_pointer(arr, target):
    arr.sort()
    start, end = 0, len(arr) - 1

    while start < end:
        now = arr[start] + arr[end]

        if now < target:
            start += 1
        elif now > target:
            end -= 1
        else:
            return True

    return False

def hash_solution1(arr, target):
    hash_table = [0] * (target + 1)
    for n in arr:
        if n <= target:
            hash_table[n] = 1

    for n in arr:
        tmp_idx = target - n
        if (tmp_idx != n
            and 0 <= tmp_idx <= target
            and hash_table[tmp_idx]):
            return True

    return False


def hash_solution2(arr, target):
    for i, n in enumerate(arr):
        tmp_target = target - n
        if tmp_target in arr[i+1:]:
            return True
    return False

       

# arr = [1,2,3,4,8]
# target = 6
# True

arr = [2,3,5,9]
target = 10
# False
print(two_pointer(arr, target))
print(hash_solution1(arr, target))
print(hash_solution2(arr, target))
