#거의 소수 구하기 
"""
min: 시작 수 , max: 종료 수 
a: 소수 리스트 

for 2 ~ 10^7
    a리스트 초기화 

for 10^7의 제곱근까지 반복:
    소수가 아니면 넘어감
    for 소수의 배숫값을 10^7까지 반복:
        현재 수가 소수가 아니라는것을 표시 

for 2~10^7:
    a리스트에서 소수인 값일 때
    temp = 현재 소수 

    #변수 표현 범위를 넘어갈수있어 이항 정리로 처리 
    while 현재 소수 <= max/temp:
        if 현재 소수 >= min/tmep: 정답값 증가 
        temp = temp * 현재 소수 

정답 출력 
"""

import math
min,max = map(int,input().split())
a = [0] * 10000001

for i in range(2,len(a)):
    a[i] = i

for i in range(2, int(math.sqrt(len(a)))+1):
    if a[i] == 0:
        continue
    for j in range(i+i,len(a),i):
        a[j] = 0

count = 0

for i in range(2,10000001):
    if a[i] != 0:
        temp = a[i]
        while a[i] <= max / temp:
            if a[i] >= min / temp:
                count += 1
                print(a[i]*temp)
            temp = temp * a[i]

print(count)