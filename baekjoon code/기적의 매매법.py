#기적의 매매법
"""
준현이는 주식을 살 수 있으면 살 수 있는 만큼 다 산다. 

성민이의 모든 거래는 전량 매도 or 전량 매수 한다. 
3일연속 가격이 상승하면 전량 매도한다. 
3일연속 가격이 하락하면 전량 매수한다. 

14일후 보유자산 = 현금 + (14일날 주가 * 주식 수)

각자 남아있는 현금, 보유한 주식 수 기록 매번 기록 
"""

import sys
input = sys.stdin.readline

cash = int(input())
stock = list(map(int,input().split()))
remain = {"JH": [cash,0] ,"SM": [cash,0]}

for s in stock: #준현
    jh_cash = remain['JH'][0]
    jh_stock = remain['JH'][1]

    jh_stock += jh_cash // s
    jh_cash %= s
    remain['JH'] = [jh_cash, jh_stock]

for i in range(3,len(stock)): #성민
    sm_cash = remain['SM'][0]
    sm_stock = remain['SM'][1]

    if stock[i-3] < stock[i-2] < stock[i-1] and sm_stock > 0: #상승->매도
        sm_cash += sm_stock * stock[i]
        sm_stock = 0
    elif stock[i-3] > stock[i-2] > stock[i-1]: #하락->매수
        sm_stock += sm_cash // stock[i]
        sm_cash %= stock[i]

    remain['SM'] = [sm_cash, sm_stock]

jh = remain['JH'][0] + (remain['JH'][1] * stock[-1])
sm = remain['SM'][0] + (remain['SM'][1] * stock[-1])
print(jh,sm,sep="  ")
if jh > sm:
    print("BMP")
elif jh < sm:
    print("TIMING")
else:
    print("SAMESAME")