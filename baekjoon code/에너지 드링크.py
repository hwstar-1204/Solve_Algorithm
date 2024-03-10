#에너지 드링크 
import sys
input = sys.stdin.readline
n = int(input())


#1
drink = list(map(int,input().split()))
drink.sort()
for i in range(n-1):
    drink[-1] += drink[i]/2
print(drink[-1])

#2
drink = sorted(list(map(int,input().split())))
drink[-1] += sum(x/2 for x in drink[:-1])
print(drink[-1])

#3
drink = list(map(int,input().split()))
max_d = max(drink)
max_d += sum(x/2 for x in drink if x != max_d)
print(max_d)