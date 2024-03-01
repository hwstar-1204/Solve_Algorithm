#이항계수 구하기1
n,k = map(int,input().split())
a = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    a[i][i] = 1
    a[i][1] = i
    a[i][0] = 1

for i in range(2,n+1):
    for j in range(1,n+1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

# for i in a:
#     print(i)

print(a[n][k])