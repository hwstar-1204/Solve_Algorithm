#소수 & 팰린드롬 수 중에서 최솟값 찾기 
"""
n : 어떤수
a : 소수 리스트 

#에라토스테네스의 채 구현 

#팰린드롬 판별 함수 구현 
팰린드롬 함수:
    숫잣값을 리스트 형태로 변환
    s: 시작 인덱스
    e: 끝 인덱스 

    while s < e:
        만약 시작과 끝 인덱스에 해당하는 값이 다르면 return False
        s,e값 증가 
    반복문 다돌았으면 return True

while True:
    n부터 값을 1씩 증가시키면서 a[i]의 값이 소수이면서 팰린드롬 수인지 판별
    맞으면 반복문 종료 
"""


import math

n = int(input())
a = [0] * (10000001)

for i in range(2,len(a)):
    a[i] = i

for i in range(2,int(math.sqrt(len(a))+1)): #제곱근 까지만 수행
    if a[i] == 0:
        continue
    for j in range(i+i,len(a),i): #배수 지우기 
        a[j] = 0

def isPalindrome(target):
    temp = list(str(target))
    s = 0
    e = len(temp) -1

    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = n
while True:
    if a[i] != 0:
        result = a[i]
        if isPalindrome(result):
            print(result)
            break
    i += 1
