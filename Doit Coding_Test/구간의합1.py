#수 n개가 주어졌을때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램 

"""
수도코드
suNo = 수의 개수 
quizNo = 합을 구해야하는 횟수 
numbers = n개의 숫자 리스트 
prefix_sum = 합 배열 변수 선언 
temp 변수 선언 

for 지정한 숫자 데이터 차례대로 탐색:
    temp에 현재 숫자 데이터 더해주기 
    합 배열에 temp값 저장 

for 질의 개수만큼 반복:
    질의 범위 받기 (s~e)
    구간의 합 출력하기(prefix_sum[j] - prefix_sum[i-1])
"""
import sys
input = sys.stdin.readline 

suNo, quizNo = map(int,input().split())
numbers = list(map(int,input().split()))
prefix_sum = [0]
temp = 0

for n in numbers:
    temp += n
    prefix_sum.append(temp)

for i in range(quizNo):
    i,j = map(int,input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
    