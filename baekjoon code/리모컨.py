#리모컨
"""
n: 이동할려는 채널 
m: 고장난 버튼 개수 
고장난 버튼 m개 

버튼 0~9 (10개), + - 

주어진 수에서 누르지 못하는 버튼은 누르지못하

1. 사용가능 리모컨 번호 리스트 만들기 
2. 주어진 채널에 최대한 가까운 수를  만들기 위한 최소한의 버튼수 
3. 그 채널에서 +나 -로 하나씩 채널을 옮기는 최소한의 수 

4. 채널 100에서 +나 -로 하나씩 채널 옮기는 경우 

2+3와 4의 경우중 최솟값을 출력 

"""
target = int(input())
m = int(input())
if m != 0:
    no_list = list(input().split())
else:
    no_list = []

ans0 = abs(target - 100)

for i in range(1000001):
    for n in str(i):
        if n in no_list:
            break
    else:
        ans0 = min(ans0,len(str(i))+abs(target-i))

print(ans0)