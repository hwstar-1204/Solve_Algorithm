#내 코드 
import time
start = time.time()
n,m = map(int,input().split()) 
card = list(map(int,input().split())) 
card.sort(reverse=True) #내림차순
total = 0

for i in range(n-2): #범위 줄이면서 
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if card[i]+card[j] >= m:
                break
            sum = card[i]+card[j]+card[k]
            if  sum<= m and sum > total:
                total = sum 
print(total)
print("time:",time.time()-start)

#acmicpc.net/source/71725177
#다른사람 코드
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# max = 0
# cards.sort(reverse=True)
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             if cards[i] + cards[j] >= m:
#                 break
#             sum = cards[i] + cards[j] + cards[k]
#             if sum <= m:
#                 if sum > max:
#                     max = sum
#                 break
# print(max)