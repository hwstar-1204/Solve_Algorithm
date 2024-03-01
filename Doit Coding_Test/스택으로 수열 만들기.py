"""
n : 수열 개수 
a : 수열 리스트 
a 수열 리스트 채우기 

for n만큼 반복:
    if 현재 수열값 >= 오름차순 자연수:
        while 현재 수열값 >= 오름차순:
            append()
            오름차순 자연수 1 증가 
            (+)저장
        pop()
        (-)저장 
    else 현재 수열값 < 오름차순 자연수:
        pop()
        if 스택 pop결과값 > 수열의 수:
            no 
        else:
            (-)저장 
if no 출력한적이 없으면 :
    저장한 값 출력 
"""

n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(n):
    su = a[i]
    if a[i] >= num:
        while a[i] >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("no")
            result = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)

