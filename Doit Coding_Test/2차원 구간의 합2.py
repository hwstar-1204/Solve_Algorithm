#2차원 구간의 합 구하기 2 11660
"""
수도 코드 
n = 리스트 크기 
m = 질의 수  
A = 원본 리스트 
D = 합의 배열 

for n만큼 반복:
    원본 리스트 저장 

for i를 1부터 n까지 반복:
    for j를 1부터 n까지 반복:
        합의 배열 저장 
        D[i][j] = D[i-1][j]+D[i][j-1]-D[i-1][j-1] + A[i][j]

for m만큼 반복:
    질의에 대한 결과 계산 및 출력 (x1,y1),(x2,y2)
    D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + A[x1-1][y1-1]    
"""
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1]+D[i-1][j]  - D[i-1][j-1] + A[i][j]

print(A,"\n")
print(D)

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)