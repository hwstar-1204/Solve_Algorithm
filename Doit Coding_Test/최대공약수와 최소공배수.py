#최대공약수와 최소공배수 
n,m = map(int,input().split())

def gcd(a,b): #재귀
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
GCD = gcd(n,m)
LCM = (n*m)//GCD
print(GCD,LCM)

#---- 라이브러리 이용
import math
g = math.gcd(n,m)
l = math.lcm(n,m)
#---- 반복문 이용 (재귀 X)
def gg(a,b):
    while b > 0:
        a,b = b,a%b
    return a
def ll(a,b):
    return (a*b)//gg(a,b)