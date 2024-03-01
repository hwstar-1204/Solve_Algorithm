"""
checkList : 비밀번호 체크 리스트 
myList : 현재 상태 리스트 
checkSecret : 몇 개의 문자와 괄녀된 개수를 충족했는지 판단하는 변수 

#함수 선언 
myadd(문자 더하기 함수):
    myList에 새로운 값을 더하고 조건에 따라 checkSecret값 업데이트 

myremove(문자 빼기 함수):
    myList에 새로운 값을 제거하고 조건에 따라 chekcSecret값 업데이트 

#메인 코드 
s : 문자열 크기 p : 부분 문자열 크기 
a : 문자열 데이터 
checkList 데이터 받기 
checkList를 탐색하여 값이 0인 데이터의 개수 만큼 checkSecret 값 증가 

P범위 (0 ~ p-1)만큼 myList 및 checkSecret에 적용하고, 유효한 비밀번호인지 판단 

for i를 p에서 s까지 반복:
    j 선언 (i-p)
    #이 부분은 myadd, myremove 함수로 별도 구현 
    한칸씩 이동하면서 제거되는 문자열과 새로 들어오는 문자열을 처리 
    유효한 비밀번호인지(checkSecret == 4) 판단해서 결과값 업데이트

결과값 출력 
"""

import sys
input = sys.stdin.readline

checkList = [0]*4
myList = [0]*4
checkSecret = 0

#함수 선언 
def myadd(c):
    global checkList, myList, checkSecret
    if c == 'a':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'c':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'g':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 't':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1
def myremove(c):
    global checkList, myList, checkSecret
    if c == 'a':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'c':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'g':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 't':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1
#main
s,p = map(int,input().split()) #문자열 크기, 부분 문자열 크기 
result = 0
a = list(input()) # 문자열 
checkList = list(map(int,input().split())) #검사 

for i in range(4): #이미 만족하는 것 처리 
    if checkList[i] == 0:
        checkSecret += 1

for i in range(p): #초기 윈도우 부분 문자열 
    myadd(a[i])

if checkSecret == 4:
    result += 1

for i in range(p,s):
    j = i - p
    myadd(a[i])
    myremove(a[j])
    if checkSecret == 4:
        result += 1

print(result)