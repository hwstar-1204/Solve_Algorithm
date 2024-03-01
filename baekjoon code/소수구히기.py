#소수구히기
import math
m,n = map(int,input().split())
a = [0] * (n+1)

for i in range(2,n+1):#!초기화
    a[i] = i
#에라토스테네스채
for i in range(2,int(math.sqrt(n)+1)): #!범위
    if a[i] == 0:
        continue
    else:
        for j in range(i+i,n+1,i): #증가정도
            a[j] = 0

for i in range(m,n+1):
    if a[i] != 0:
        print(a[i])
