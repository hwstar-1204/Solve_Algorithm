#최대 공약수 gcd() 함수 구현
"""gcd(a,b):
    if b == 0 이면
        a가 최대공약수 
    else:
        gcd(작은수,큰수%작은수)

t (테스트 케이스)

for t만큼 반복:
    a: 1번째 수 , b: 2번째 수 
    결괏값 = a*b/gcd(a,b)
    결괏값 출력 
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

t = int(input())


for i in range(t):
    a,b = map(int,input().split())
    result = a*b/gcd(a,b)
    print(int(result))