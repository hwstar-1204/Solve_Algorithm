#포도주 서식
"""
포도주 시식 규칙
1. 포도주 선택하면 다 마셔야하고 마신 후 원래위치에 놓아야함 
2. 연속으로 놓인 3잔을 모두 마시는건 안됨 

target: 최한 많은 양의 포도주를 맛보기 
do: 어떤 포도주 잔을 선택해야하지?

입력: n 잔개수, 1~n개의 포도주잔 , 각 잔에 들어있는 양 (1<=n<=10000)
출력: 최대로 마실수 있는 포도주 양 

# XXXX
3개를 한그룹으로 생각
2*(n/3) + n%3

1 8 4 3 100 200
1 8 , (3,100 or 100,200 or 3 200)
1 4 , (100,200)
8 4 , (100, 200)
# XXXX


 
6 10 13 9 8 1
1마실때 (9까지마신양 + 1),(13까지마신양+1+8)
1안마실때 8까지마신양 

6 16 23 28 33 33 
dp[3] = 6+13 or 10+13+0 or 16 = 23 
dp[4] = 9+16 or 13+9+6 or 23 = 28
dp[5] = 8+23 or 9+8+16 or 28 = 33
dp[6] = 1+28 or 8+1+23 or 33 = 33 

sudo 
n = 포도주 잔 개수 
arr = 포도주 한잔씩 최대로 마실 수 있는 양 저장 리스트 (n)

포도주 0개일떄 최대 양 = 0
포도주 1개일때 최대 양 = arr[1]
포도주 2개일때 최대 양 = arr[1] + arr[2]
포도주 3개일때 최대 양 = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])

for dp range(3 ~ n):
    amount = n번째 포도주 양
    a = i번째 포도주 + i-2번째까지의 최대양
    b = i번째 포도주 + i-1번째 포도주 + i-3번째까지의 최대양
    c = i-1번째까지의 최대양
    dp[i] = max(a,b,c)
print(max(dp))

"""
import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*10000
for i in range(n):
    arr[i]=int(input())
dp = [0]*10000

dp[0] = arr[0]
dp[1] = arr[0]+ arr[1]
dp[2] = max(arr[0]+arr[2], arr[1]+arr[2], dp[1])

for i in range(3,n):
    a = arr[i] + dp[i-2]
    b = arr[i] + arr[i-1] + dp[i-3]
    c = dp[i-1]
    
    dp[i] = max(a,b,c)

print(max(dp))
