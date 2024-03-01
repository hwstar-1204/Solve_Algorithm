#절대값 힙 구현하기 
"""
n: 연산횟수 
arr: 입력받은 정수를 저장하는 배열 (우선순위 큐)

우선순위 큐 선언
- 절대값 기준으로 정렬되도록 설정
- 단, 절대값이 같으면 음수 우선 정렬

for i가 n이 될때까지:
    x: 연산과 관련된 정보를 나타내는 정수 (입력받음)
    
    if x == 0:
        if arr:
            큐에서 front값 출력 (get) 
            그 값을 큐에서 제거 
        else:
            0 출력 
    else:
        put으로 큐에 새로운값 추가 하고 정렬기준에 따라 자동 정렬 (put)
"""

# from queue import PriorityQueue
# import sys
# print = sys.stdout.write
# input = sys.stdin.readline
# n = int(input())
# myqueue = PriorityQueue()

# for i in range(n):
#     request = int(input())
#     if request == 0:
#         if myqueue.empty():
#             print("0\n")
#         else:
#             temp = myqueue.get()
#             print(str(temp[1])+'\n')
#     else:
#         myqueue.put((abs(request),request))

from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline
n = int(input())
myqueue = PriorityQueue()


for i in range(n):
    request = int(input())

    if request == 0:
        if myqueue.empty():
            print("0\n")
        else:
            temp = myqueue.get()
            print(str(temp[1]) + "\n")

    else:
        myqueue.put((abs(request),request))
