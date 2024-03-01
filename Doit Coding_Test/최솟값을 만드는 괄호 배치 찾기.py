#최솟값을 만드는 괄호 배치 찾기 
"""
answer = 정답 변수 
a 리스트 (들어온 데이터를 '-' 기호를 기준으로 split)

#현재 string에 있는 수를 모두 더하는 함수 구현 
mysum():
    현재 들어온 string 값을 "+" 기호 기준으로 split 수행 
    for 나뉜 데이터 개수 만큼 반복:
        string값을 integer형으로 변환해 리턴값에 더하기 
    전체 합 리턴

for i를 a만큼 반복하기 
    결괏값 = mysum(a[i])
    if 가장 앞 데이터일때:
        answer에 결괏값 더하기 
    else:
        answer에 결괏값 빼기 

answer 출력 
"""

answer = 0
a = list(map(str,input().split('-')))

def mysum(i):
    sum = 0
    tmp = i.split('+') # 나눈것을 바로 리스트로 전달하나봄
    for t in tmp:
        sum += int(t)
    return sum 

for i in range(len(a)):
    result = mysum(a[i])
    if i == 0:
        answer += result 
    else:
        answer -= result 

print(answer)