#제곱이 아닌 수 찾기 
"""
min: 최솟값 max: 최댓값 
check(min~max 사이에 제곱수 판별 리스트 )

for i = 2 ~ max의 제곱근:
    pow(제곱수)
    start_index(최솟값/제곱수) #나머지가 있는경우 1을 더함 
    for j = start_index ~ max 사이 반복: #제곱수의 배수 형태로 탐색
        j * pow가 max보다 작을 때 최솟값, 최댓값 사이의 제곱수이므로 
        check 리스트에 저장 

count (제곱이 아닌 수 카운트)

for 0 ~ max-min:
    check 리스트에서 제곱이 아닌 수라면 count 증가 

count 출력
"""

import math
min,max = map(int,input().split())
check = [False] * (max-min+1)

for i in range(2,int(math.sqrt(max)+1)):
    pow = i*i
    start_index = int(min/pow)
    if min % pow != 0:
        #나머지가 있는 경우 1을 더해 min보다 큰 제곱수에서 시작하도록 설정
        start_index += 1
    for j in range(start_index, int(max/pow)+1):
        check[int((j*pow)-min)] = True

count = 0

for i in range(0,max-min+1):
    if not check[i]:
        count += 1

print(count)