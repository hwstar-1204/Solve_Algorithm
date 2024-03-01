#분해합
n = int(input())
for i in range(1,n+1): 
    tmp = sum(int(i) for i in str(i)) #각 자리수의 합
    if i+tmp == n:
        print(i)
        break
else:
    print(0)