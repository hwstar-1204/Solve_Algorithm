#가장 긴 짝수 연속한 부분 수열(small)
"""
주어진 수열s 에서 최대 k번 원소 삭제
최대로 짝수 연속한 부분 수열 찾기 

0~k번 삭제 하면서 가장 긴 짝수 수열 찾기 
각 반복에서 삭제한 부분까지의 최대 짝수 수열 저장
다음 번에서 위의 정보 이용

0101 0101
1020 2020 #짝수면 이전 자기자신값-1 홀수면 이전 배열에서 왼쪽+오른쪽

2 3 5 6 8 9 10 11 12 14 16 19
1 0 0 1 1 0 1  0  1  1  1  0

1 2 3 4 5 6 7 8            
"""
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
s = list(map(int,input().split()))

end = 0 # 투포인터의 끝
odd = 0 # 홀수 개수 
now = 0 # 현재 만드는 수열
max_len = 0 #짝수 수열 최대 길이 (정답)

for start in range(n):
    while (odd <= k and end < n):
        if s[end]%2: #홀수
            if odd == k:
                break
            odd += 1
        now += 1
        end += 1
    
    if max_len < now - odd:
        max_len = now - odd
    if s[start] % 2:
        odd -= 1
    
    now -= 1

print(max_len)

