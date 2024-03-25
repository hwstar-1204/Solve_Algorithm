#카드 2
"""
카드 개수: n
카드는 맨위에 1 맨 아래는 n
행동순서
1. 맨위 카드 버림
2. 맨위 카드를 맨 아래로 놓는다. 

1장이 남을때까지 반복 
출력: 마지막 한장의 카드 번호

sudo
cards = 1~n까지 카드 리스트 

while 카드 리스트 개수가 1개일때까지:
    맨위 카드를 버림
    맨위 카드를 맨 아래로 놓는다. 

"""
from collections import deque

n = int(input()) 
card_deque = deque(range(1,n+1))

while len(card_deque) > 1:
    card_deque.popleft()
    top = card_deque.popleft()
    card_deque.append(top)

print(card_deque.pop())