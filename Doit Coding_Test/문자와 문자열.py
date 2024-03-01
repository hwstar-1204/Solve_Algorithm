#칸토어 집합

"""
n=0              #1개 
n=1 3일때 2       #3^0부터 3^0개
n=2 9일때 4 5 6   #3^1부터 3^1개
n=3 27일때 10~19  #3^2부터 3^2개 
"""

"""

list = 3^n * "-"
answer = '' 

BFS(3**n개 - 문자열):
    if 길이가 1이면:
        return "-"

    list에서 중간부분 ' ' 으로 바꾸기 
    # while 두번째가 ' '아 아닐때까지 
    answer += 왼쪽 재귀 + 중간부분 +오른쪽 재귀 
    return answer
"""

import sys
input = sys.stdin.readline

def canto(string,n):
    if n <= 0:
        return string
    
    mid = 3**(n-1)
    for i in range(mid,2*mid): #중간 부분 지우기
        string[i] = ' ' 
    return canto(string[0:mid],n-1) + string[mid:2*mid] + canto(string[2*mid:3*mid],n-1)
    

while True:
    try:
        num= int(input())
        input_str = ['-'] * (3**num)

        answer = canto(input_str,num)
        print(*answer,sep='')
    except:
        break