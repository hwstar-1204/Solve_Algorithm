# 좌표 정렬하기 
#(1) 
# n = int(input())
# nums = []

# for _ in range(n):
#     x,y = map(int,input().split())
#     nums.append((x,y))

# nums.sort(key=lambda x: (x[0],x[1]))
# for a,b in nums:
#     print(a,b)

#(2)
n = int(input())
nums = []

for _ in range(n):
    x, y = map(int,input().split())
    nums.append((x + 100000, y + 100000))

count = [0] * 200001
for x, y in nums:
    count[x] += 1

sorted_nums = []
for i in range(len(count)):
    sorted_nums.extend([(i - 100000, y - 100000) for x, y in nums if x == i])

for a, b in sorted_nums:
    print(a, b)