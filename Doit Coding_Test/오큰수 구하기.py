#오큰수 구하기 
"""
n: 수열 개수 
a: 수열 리스트 
ans: 정답 리스트 
a 수열 리스트 채우기 
mystack 스택 선언 

for i를 n만큼 반복:
    while 스택이 비지 않고, 현재 수열값이 top에 해당하는 수열보다 클 때까지:
        스택에서 pop한 값을 index로 하는 정답 리스트 부분을 수열 리스트의 현재 값(a[i])으로 저장
    스택에 i의 값을 저장 

while 스택이 빌 때까지:
    스택에 있는 index의 정답리스트에 -1저장 

정답 리스트 출력 
"""

n = int(input())
ans = [0] * n 
a = list(map(int,input().split()))
mystack = []

for i in range(n):
    while mystack and a[mystack[-1]] < a[i]:
        ans[mystack.pop()] = a[i]
    mystack.append(i)

while mystack:
    ans[mystack.pop()] = -1

result = ""

for i in range(n):
    result += str(ans[i]) + " "

print(result)

