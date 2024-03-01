#회의실 배정하기 
"""
n: 회의 개수 
a: 회의 정보 저장

a 리스트 정렬 수행 #종료 시각 기준으로 정렬,
종료 시각이 같으면 시작 시각 기준 정렬 

for 회의실의 개수만큼 반복:
    if 앞 회의의 종료 시각보다 시작 시간이 늦은 회의가 나온 경우:
        현재 회의의 종료 시각으로 종료 시각 업데이트 
        진행할 수 있는 회의 수 1 증가 
총 진행 가능한 회의 수 출력
"""

n = int(input())
a = [[0] * 2 for _ in range(n)]

for i in range(n):
    s,e = map(int,input().split())
    a[i][0] = e #종료시각 우선 정렬이므로 0번째에 종료 시각 먼저 저장
    a[i][1] = s 

a.sort() #종료시각 기준 오름차순 정렬
count = 0
end = -1 

for i in range(n):
    if end <= a[i][1]:
        end = a[i][0] #mistake
        count += 1
print(count)