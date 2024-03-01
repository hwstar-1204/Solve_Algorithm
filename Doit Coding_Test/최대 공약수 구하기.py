#최대 공약수 구하기 
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

a,b = map(int,input().split())
result = int(gcd(a,b))

print(result*"1")

# while result > 0:
#     print(1,end='')
#     result -= 1