#계단오르기 

"""
한번에 한칸,두칸 오를 수 있다. 
마지막 계단을 밟아야 한다. 
연속된 3칸을 오를수없다. 
계단에 쓰인 점수 총합의 최대값일 때를 구하라 

마지막칸에서의 최대값 = 이전칸까지의 최대값 + 마지막칸 or 전전칸까지의 최대값+마지막칸
0 -> 0
1 -> 첫번째칸 점수
2 -> 두번째 칸 점수 

3-> 첫번째칸에서 온경우+3번째칸 점수 or 2번째칸에서 온경우+3번째칸 점수 (비교)
1-3
2-3

1-3-4
2-3-4 = 2번째까지의칸 + 3번째칸 + 4번째칸이 지금 구한 최대값이랑 같으면 
    -> 3계단 연속오른거니까 취소 
"""
import sys
input = sys.stdin.readline

n = int(input())
stair = [0] * (301)
for i in range(1,n+1):
    stair[i] = int(input())

max_stair = [0]*(301)
max_stair[1], max_stair[2] = stair[1], stair[1]+stair[2] #1,2,3 최대값 초기화 

for i in range(3,n+1):
    d1 = max_stair[i-3] + stair[i-1] + stair[i] #3번째전,이전+현재
    d2 = max_stair[i-2] + stair[i] #2번째전,현재

    max_stair[i] = d1 if d1 > d2 else d2

print(max_stair[n])