# 숫자 카드 2 
"""
숫자 카드 N개 가지고 있다. 
정수 M개가 주어질때 이 수가 적혀있는 숫자 카드를 몇개 가지고 있는지 구하기 

입력
N: 가지고 있는 카드의 수 
숫자카드에 적혀있는 정수들 (-10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.)
M: 주어진 숫자 (1 ≤ M ≤ 500,000)
몇개 가지고 있는 숫자 카드인지 구해야할 M개의 정수들 
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
card_list = list(map(int,input().split()))
m = int(input())
find_list = list(map(int,input().split()))

card_dict = defaultdict(int)
for card in card_list:
    card_dict[card] += 1

# for find in find_list:
#     if find in card_dict:
#         print(card_dict[find],end=' ')
#     else:
#         print(0, end=' ')

result = [str(card_dict[find]) for find in find_list]
print(' '.join(result))
