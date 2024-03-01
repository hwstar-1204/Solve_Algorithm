#배열에서 k번째 수 찾기 
"""
1 2 3 
2 4 6 
3 6 9 

n: 리스트 크기 
k: 구하고자하는 index
start = 1
end = k

#이진 탐색 
while start <= end:
    middle: 중간 인덱스 
    cnt: 중간값 보다 작은 수 
    #중간값보다 작은 수 계산
    for i는 1~n:
        cnt에 중앙 인덱스를 i로 
"""

n = int(input())
k = int(input())
start = 1
end = k
ans = 0

while start <= end:
    middle = int((start+end)/2)
    cnt = 0
    for i in range(1,n+1):
        cnt += min(int(middle/i),n)
    if cnt < k:
        start = middle+1
    else:
        ans = middle
        end = middle-1

print(ans)