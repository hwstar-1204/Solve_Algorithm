#서강근육맨
"""
n: 운동기구 개수 
한번에 최대한 두개 기구 선택
이전에 선택안한 운동기구 선택

자극이 잘오면 근손실 커짐 
pt 한번 받을때 근손실 정도가 m을 넘으면 안됨 
m의 최솟값을 구하라 

운동기구는 두개씩 선택해서 다쓰는데 근손실 m은 넘지않게 운동해야함
선택한 운동기구 근손실 합 < M 

홀수개이면
최소  가장 근손실큰거 <= m


1 2 30 40 50 60 
1 3 25 30 40 50 

10 15 20 40 90 100 101
111 115 110 ? 101 -> 115
짝수이면 맨앞 맨뒤 짝지어서 작아지기 전까지 반복
홀수이면 맨뒤 빼고 맨앞 맨뒤 짝지어서 마지막에 맨뒤값이랑 비교 

10 15 70 80 90 100 101 
101 빼고 150

"""
import sys
input = sys.stdin.readline
n = int(input())
m = sorted(list(map(int,input().split())))

even = n % 2 #짝수=0 , 홀수=1

def match_pt(r,flag):
    max_loss = 0
    for i in range(r):
        tmp = m[i] + m[-1-i-flag]
        max_loss = tmp if tmp > max_loss else max_loss
    return max_loss

if even: # 홀수
    result = match_pt((n-1)//2,even)
    print(m[-1] if result < m[-1] else result)
else:
    print(match_pt(n//2,even))