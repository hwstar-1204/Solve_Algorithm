#카드 게임 
"""
n: 카드 개수 
deque: 카드 넣을 큐 선언 
answer: 마지막 남은 카드 번호 

for i가 n될때까지:
    deque에 i 삽입 

while 큐에 하나 남을때 까지:
    큐에서 popleft(왼쪽 삭제) 
    second = 큐에서 삭제한 값(두번쨰 삭제값)
    큐에 second 추가 (append)

asnwer = deque에서 삭제 
"""

from collections import deque
n = int(input())
mydeque = deque()

for i in range(1,n+1):
    mydeque.append(i)

while len(mydeque) > 1:
    mydeque.popleft()
    second = mydeque.popleft()
    mydeque.append(second)

print(mydeque[0])