# 2+1 세일
import sys
input = sys.stdin.readline
n = int(input())
money = sorted([int(input()) for _ in range(n)],reverse=True)

def calc_m(flag):
    answer = 0
    for i in range(n//3+flag):
        answer += money[3*i] + money[3*i+1]
    return answer

if n % 3 == 1: #3개씩 묶고 뒤에 한개 남았을때
    print(calc_m(0) + money[-1])
elif n % 3 == 2:
    print(calc_m(1))
else:
    print(calc_m(0))

#--------------------------------------------------------------------

#(2)
import sys
input = sys.stdin.readline
n = int(input())
money = [int(input()) for _ in range(n)]
money.sort(reverse=True)

cnt = n // 3 # 2+1 묶음 개수 
total = sum(money)

sale = 0
for i in range(2,n,3):
    sale += money[i]

print(total - sale)


# 8 7 6/ 5 4 3/ 2 1

