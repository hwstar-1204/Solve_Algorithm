n,m = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(m):
    i,j,k = map(int,input().split())
    select = sorted(arr[i-1:j])[k-1]
    print(select)