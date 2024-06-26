# 웰컴 키트 
"""
티셔츠 6가지 종류, 같은 사이즈의 T장 묶음으로만 주문
볼펜은 한종류, P자루씩 묶음으로 주문하거나 1자루씩 주문

조건
티셔츠: 남아도 되지만 부족해서는 안되고 신청한 사이즈대로 나눠주기
볼펜: 남거나 부족해서 안되고 정확히 참가자 수 만큼 준비

입력
1. 참가자 수 N
2. 티셔츠 사이즈별 신청자의수 6개가 공백으로 구분 
3. T: 정수 티셔츠 묶음 수, P: 펜의 묶음 수 

출력
1. 티셔츠를 T장씩 최소 몇묶음 주문해야하는지 
2. 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지와 그때 펜의 한자루씩 몇개 주문하는지 
"""

n = int(input())
size_list = list(map(int,input().split()))
t, p = map(int,input().split())

t_bundle = 0

for i in size_list:
    if i % t == 0:
        t_bundle += i // t
    else:
        t_bundle += (i // t) + 1

print(t_bundle)
print(n//p, n%p)
