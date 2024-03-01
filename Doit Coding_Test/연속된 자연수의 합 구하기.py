"""
n 변수 저장 
사용 변수 초기화 (count=1, start_index=1, end_index=1, sum=1)

while end_index != n:
    if sum == n : 경우의 수 증가 , end_index증가 , sum값 변경 
    if sum > n : sum값 변경, start_index 증가 
    else: end_index 증가 sum값 변경 
"""

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)