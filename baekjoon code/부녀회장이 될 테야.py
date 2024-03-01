#부녀회장이 될 테야 
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input()) #층수,호수
    n = int(input())

    a = [[0]*(n+1) for _ in range(k+1)]
    for i in range(n+1):
        a[0][i] = i

    for i in range(1,k+1):
        for j in range(1,n+1):
            a[i][j] = a[i-1][j] + a[i][j-1]
    print(a[k][n])

    #?층 1호 = 1명
    #a층 b호 = a-1층 1~b호 의 합 
    #a층 b+1호 = a-1층 1~b+1호의 합 
    
    #0 1 2 3 
    #0 1 3 6 