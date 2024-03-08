# 연속합 
"""
10, -4, 3, 1, 5, 6, -35, 12, 21, -1

1       2       3       4       5
12      23      34      45
123     234     345
1234    2345
12345

10 -4 3 1 5
6  -1 5 6
5  4  

"""
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))

for i in range(1,n):
    nums[i] = max(nums[i],nums[i-1]+nums[i])
print(max(nums))

# dp = [nums[i] + nums[i+1] for i in range(n-1)]
# answer = max(max(nums),max(dp))

# j = 1
# while lop:= n - j:
#     for i in range(lop-1):
#         tmp = nums[i] + dp[i+1]
#         if tmp > answer:
#             answer = tmp
#         dp[i] = tmp
#     j += 1

# print(answer)