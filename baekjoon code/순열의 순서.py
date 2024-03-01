#순열의 순서
"""
작은수부터 앞에, 같으면 두번째가 더 작은것 
1 2 3 4
1 2 4 3
1 3 2 4 vvv
1 3 4 2
1 4 2 3
1 4 3 2

1 
2 2*1
6 3*2
24 4*6 #자기 인덱스*이전값

# 이전 배열개수의 배수보다 작은값 : 몇배수 == 시작 숫자 
1번째 <=2
2번째 <=2
3번째 값 <= 4
#4번째값 = 
#5번째 값 <= 6
#6번째 = 
번째값 // n-1순열개수 +1 == (맨앞) ?번째로 작은수
이전 순열의 배수이면 번째값 // 이전순열개수

위에서 쓰인 값 제거 # 2 3 4 
그다음은 번째값 // n-2순열 개수 +1 번째로 작은수 

위에서 쓰인 값 제거 # 2 4
그다음은 번째값 // n-3순열 개수 + 1 번째로 작은 수 

...

개수가 2개 남으면
홀수번째이면 작은순서대로 
짝수번째이면 큰순서대로 



"""


import sys
input = sys.stdin.readline
n = int(input()) #1~n 숫자 개수
op = list(map(int,input().split())) 

n_list = [ i for i in range(n+1)] #순열 리스트      0 1 2 3 4
n_cnt = [1 for _ in range(n+1)] #n에 따른 순열 개수  0 1 2 6 24
for i in range(1,n+1):
    n_cnt[i] = n_cnt[i-1] * i

def op1(k,length): #1이면 k번째 순열 출력
    answer = []

    while length > 2: 
        idx = k // n_cnt[length-1] + 1
        if k % n_cnt[length-1] == 0:
            idx -= 1

        answer.append(n_list[idx]) #번째
        del n_list[idx]
        length -= 1

    del n_list[0]
    if k%2 == 1:
        answer += n_list
    else:
        answer += n_list[::-1] 
    print(*answer)

def op2(permute,length): # 2이면 몇번째 순열인지 출력 
    answer = 0

    for i in permute:
        if length > 0:
            idx = n_list.index(i)
            length -= 1
            answer += n_cnt[length] * (idx-1)
            del n_list[idx]
        # 1 3 2 4 -> 3
        # 0
    print(answer+1) 

if op[0] == 1:
    op1(op[1],n)
else:
    pass
    op2(op[1:],n)