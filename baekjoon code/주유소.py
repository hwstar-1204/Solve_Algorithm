# 주유소

"""
1km가는데 1L가 필요하다.
출발할때 첫번째 도시에서 주유해야한다. 
주유비용이 최소가 되도록한다. 

-> 처음 주유할때 최소비용은 
최소 다음 도시까지 가는 거리 * 현재 도시 주유 비용 < m < 끝 도시까지 가는거리 * 현재 도시 주유 비용 

2 3 1 5
5 2 4 1 3

0~끝 순서로 도시까지 각각의 도시에서 최소비용을 구하는것은 음
if 지금까지 가장 싼 기름값 * (다음 도시까지 거리) (비교) 가장 싼 기름값보다 싼 기름값나오면 * (다음도시까지 거리 생략)
    그 도시부터 해당 기름값으로 계산 
"""
import sys
input = sys.stdin.readline
n = int(input()) # 도시 개수
km = list(map(int,input().split())) # 다음 도시까지의 거리 (n-1개)
oil = list(map(int,input().split())) # 해당 도시의 기름값
min_cost = float('inf')
answer = 0

#그리디
for k,cost in zip(km,oil):
    if cost < min_cost:
        min_cost = cost
    answer += min_cost * k

print(answer)    

#동적 계획법
# dp = [0 for _ in range(n-1)]
# dp.append(km[0] * oil[0])

# for i, (k,cost) in enumerate(zip(km,oil), 1):
#     if cost < min_cost:
#         min_cost = cost
    
#     dp[i] = dp[i-1] + min_cost * k
# print(dp[n-1])