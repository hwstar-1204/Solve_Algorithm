#약수 
import sys
sys.setrecursionlimit(10*6)
n = int(input())
n_list = list(map(int,input().split()))
def gcd(a,b): #최대 공약수
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
n_min = min(n_list)
n_max = max(n_list)
result = (n_min*n_max)//gcd(n_max,n_min)#최소공배수

if result in n_list:
    print(result*n_min)
else:
    print(result)