#이항계수 구하기 2

n,k = map(int,input().split())
a = [[0]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    a[i][i] = 1
    a[i][0] = 1
    a[i][1] = i 
for i in range(2,n+1):
    for j in range(n+1):
        a[i][j] = a[i-1][j-1] + a[i-1][j]
        a[i][j] %= 10007
print(a[n][k])

# for i in a:
#     print(i)
