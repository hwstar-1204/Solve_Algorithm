#블루레이 만들기 
"""
n: 레슨 개수 저장
m: 블루레이 개수 저장 
a: 기타 레슨 데이터 저장 리스트 
start = 시작 인덱스
end = 종료 인덱스 

for a 리스트 탐색:
    시작 인덱스 저장 (a리스트 중 최댓값)
    종료 인덱스 저장 (a리스트의 총합)

while 시작 인덱스 <= 종료 인덱스:
    middle(중간 인덱스)
    sum:  레슨 합 
    count: 현재 사용한 블루레이 개수 
    for n의 개수 만큼 반복:
        if sum + 현재 레슨 시간 > 중간 인덱스:
            count값을 올리고 
            sum을 0으로 리셋
        sum에 현재 레슨 시간값 더하기 

    sum이 0이 아니면 마지막 블루레이가 필요하므로 count값 올리기 

    if count > M:
        start = M+1
    else:
        end = m-1

시작인덱스 출력 
"""

n,m = map(int,input().split())
a = list(map(int,input().split()))
start = max(a)
end = sum(a)

while start <= end:
    middle = int((start+end)/2)
    sum = 0
    count = 0
    for i in range(n):
        if sum + a[i] > middle:
            count += 1
            sum = 0
        sum += a[i]
    if sum != 0:
        count += 1
    if count > m:
        start = middle + 1
    else:
        end = middle - 1

print(start)

