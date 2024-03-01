#확장 유클리드 호제법 
"""
a: 1번째 수 
b: 2번째 수
c: 3번째 수 

gcd 함수 

#유클리드 호제법 함수 구현 
Execute(a,b):
    if b == 0: 재귀함수를 중단하고, x,y를 각각 1,0으로 설정하여 return 
    q: a를 b로 나눈 몫
    Execute(b, a%b) #재귀함수 
    x = 이전y값 , y = 이전x - (이전y)*몫 을 계산하는 역산 로직 구현
    #재귀에서 빠져나오는 영역에서 실행하면 자연스럽게 역순이 됨 
    계산된 x y return 

최대 공약수  = gcd(a,b)

if c가 최대 공약수의 배수가 아니면:
    -1 출력
else:
    나머지(b)가 0이 될때까지 재귀함수를 호출하는 유클리드 호제법 함수 호출 
    결괏값에 c/최대공약수의 값을 곱한 후 해당 값을 출력 
"""

a,b,c = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def Execute(a,b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a//b
    v = Execute(b,a%b)
    ret[0] = v[1]
    ret[1] = v[0] - v[1]*q
    return ret

mgcd = gcd(a,b)

if c % mgcd != 0:
    print(-1)
else:
    mok = int(c/mgcd)
    ret = Execute(a,b)
    print(ret[0]*mok,end='')
    print(ret[1]*mok)