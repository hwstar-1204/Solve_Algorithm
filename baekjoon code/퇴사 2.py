#퇴사 2
"""
n+1일째 되는날 퇴사하기 위해 n일 동안 최대한 많은 상담하기  
T: 각각 상담을 완료하는데 걸리는 기간
P: 상담했을때 받을 수 있는 금액 

n일에 T기간 걸리는 상담을 하면 다음 상담은 n+T번째 상담부터 가능하다. 
상담 기간이 n을 넘어가는 상담은 하지 못한다. 

입력: n(상담할수있는 기간), n일 동안의 T,P 순서대로 주어짐 
    (1<=n<=1,500,000) (1<=T<=50) (1<=P<=1,000)
출력: 최대 수익

i일에 i번쨰 상담을 진행할때/진행 안할때의 수익을 비교해서 dp[i]에 저장 
재귀형태, 제한시간 2초 안에 n은 1,500,000 ...

sudo 
info = 상담 정보 리스트 = [0, (T,P)...]
dp = 수익 저장 리스트 = [0]*(n+1)

def calc_cost(n = 상담 가능 지점):
    cost = 0
    t,p = info[n]
    d = n일 상담 진행할때 + p (다음 n = n+t)
    dn = n일 상담 진행 안할때 (다음 n = n+1)
        
    return max(d,dn)
calc_cost(1)
"""
import sys
input = sys.stdin.readline

n = int(input())
info = [(0,0)]
dp = [0] * (n+1)

for i in range(n):
    t,p = map(int,input().split())
    info.append((t,p)) # 기간,수익

for i in range(n+1):
    term, profit = info[i]
    dp[i] = max(dp[i], dp[i-1])

    if i + term - 1 <= n:
        dp[i+term-1] = max(dp[i+term-1], dp[i-1]+profit)

print(max(dp))


# def calc_cost(today): #10
#     #today == n이면 접근 가능 
#     #today > n 이면 접근 불가 
#     if today > n:
#         return 0
    
#     term,profit = info[today] #1 10
#     if today + term > n:
#         return 0
    
#     d = calc_cost(today+term) + profit  # 상담 진행 O
#     dn = calc_cost(today+1)             # 상담 진행 X

#     cost = max(d,dn)

#     return cost

# print(calc_cost(1))