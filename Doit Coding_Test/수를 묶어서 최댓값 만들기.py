"""
n: 카드 묶음 개수 
pluspq : 양수 우선순위 큐
minuspq : 음수 우선순위 큐 
one: 1의 개수 카운트  
zero : 0의 개수 카운트 

for n만큼 반복:
    #양수 우선순위큐는 내림차순 정렬을 위해 -1을 곱하여 저장 
    데이터를 4개의 그룹에 분리 저장 

#양수 우선순위 큐 처리 
while 양수 우선순위 큐 크기가 2보다 작을때까지 
    수 2개를 묶어서 큐에서 뽑음 (뽑은 수는 -1을 곱함)
    2개의 수를 곱한 값을 결과값에 더함 

if 양수 우선순위 큐에 데이터가 남아있으면:
    해당 데이터를 결과값에 더함 

#음수 우선순위 큐 처리 
while 음수 우선순위 큐 크기가 2보다 작을때까지 
    수 2개를 묶어서 큐에서 뽑음
    2개 수를 곱한 값을 결과값에 더함 

if 음수 우선순위 큐에 데이터가 남아있고 데이터 0이 1개도 없으면:
    해당 데이터를 결과값에 더함 
###음수 데이터가 남아있는데 데이터 0이 있는경우는 남은 음수 데이터를 처리하지 않음으로써 무시하는 효과 !!!!

숫자 1의 개수를 결과값에 더함
결과값 출력 
"""

from queue import PriorityQueue
n = int(input())
pluspq = PriorityQueue()
minuspq = PriorityQueue()
one = 0
zero = 0
result = 0

for i in range(n):
    tmp = int(input())
    if tmp > 1: #mistake
        pluspq.put(tmp*-1)
    elif tmp < 0:
        minuspq.put(tmp)
    elif tmp == 1:
        one += 1
    else:
        zero += 1

#양수 우선순위 큐 처리 
while pluspq.qsize() > 1:
    a = pluspq.get() * -1
    b = pluspq.get() * -1
    result += a*b

if pluspq.qsize() > 0:
    result += pluspq.get() * -1 #mistake

#음수 우선순위 큐 처리 
while minuspq.qsize() > 1:
    a = minuspq.get()
    b = minuspq.get()
    result += a*b

if minuspq and not zero:
    result += minuspq.get()

result += one
print(result)

