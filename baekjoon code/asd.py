n = int(input())
a = list(map(int,input().split()))

# a,b,c
# (a+b+c)/a*100   / 3
# 100(b+c) + a

print(((sum(a)/max(a))*100)/n)