#다음 순열 
""""
N: 1~까지의 수 
처음엔 오름차순 
마지막은 내림차순  

P: 다음 순열 입력  (마지막 순열==이미 오름차순이면 -1 출력 )

1~n수를 오른차순하게 초기화 리스트 
1. 맨뒤와 맨뒤에서 두번째 교체 
2. 맨뒤꺼 맨앞으로 
3. 1번내용 
4. 맨앞꺼 맨 뒤로 
5. 1번내용 
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

for i in range(1,n+1):
    queue.append(i)

print(queue)
queue.

