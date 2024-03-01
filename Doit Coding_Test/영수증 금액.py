n,m = map(int,input().split())
answer = [[0]*m for _ in range(n)]
for _ in range(2):
    for i in range(n): #행 개수만큼 반복
        temp = list(map(int,input().split()))
        
        for j in range(m):
            answer[i][j] += temp[j]

for i in answer:
    print(i,end=' ')
