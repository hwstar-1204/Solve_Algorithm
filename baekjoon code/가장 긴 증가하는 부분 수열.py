#가장 긴 증가하는 부분 수열 

# DP
n = int(input())
num_list = list(map(int,input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    for j in range(i):
        if num_list[j] < num_list[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(max(dp))

#이분탐색
n = int(input())
num_list = list(map(int,input().split()))
bin_arr = [num_list[0]]

def binary_search(arr,value):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < value:
            left = mid+1
        else:
            right = mid
    return left

for i in range(1,n):
    now = num_list[i]
    if bin_arr[-1] < now:
        bin_arr.append(now)
    else:
        index = binary_search(bin_arr,now)
        bin_arr[index] = now

print(len(bin_arr))