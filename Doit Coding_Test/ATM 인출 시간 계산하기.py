#ATM 인출 시간 계산하기 
"""
n: 사람 수
a: 자릿수별로 구분해 저장한 리스트
s: 합 배열 : 각 사람이 인출을 완료한는데 필요한 시간을 저장

for i를 1~n만큼 반복:
    for j를 i-1~0까지 뒤에서부터 반복:
        현재 범위에서 삽입 위치 찾기 
    for j를 i~insert_point+1까지 뒤에서부터 반복:
        삽입을 위해 삽입 위치에서 i까지 데이터를 한칸씩 뒤로 밀기 
    삽입 위치에 현재 데이터 저장 

for i를 1-n만큼 반복:
    a리스트를 통한 합 배열 s 만들기 

s 리스트의 각 데이터값을 모두 합해 결과 출력 

"""

n = int(input())
a = list(map(int,input().split()))
s = [0]*n

for i in range(n):
    insert_point = i
    insert_value = a[i]
    for j in range(i-1,-1,-1):
        if a[j] < a[i]:
            insert_point = j+1
            break
        if j == 0:
            insert_point = 0
    for j in range(i,insert_point,-1):
        a[j] = a[j-1]
    a[insert_point] = insert_value

s[0] = a[0]

for i in range(1,n):
    s[i] = s[i-1] + a[i]

sum = 0

for i in range(0,n):
    sum += s[i]

print(sum)