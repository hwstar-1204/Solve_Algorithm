#큐2
"""
큐 자료구조 만들기 
a = []
b = []
push이면 입력값을 a 뒤에 append , b 앞에 insert(0, )
pop이면 b에서 pop한 값을 a에서 remove 
size이면 len(a)
empty이면  0 if len(a) else 1
front이면 a[0], -1 if not len(a)
back이면 a[-1] -1 if not len(a)
"""
# import sys
# input = sys.stdin.readline

# n = int(input())
# a,b = [], []


# for _ in range(n):
#     cmd = list(input().split())
#     flag = len(a)

#     if cmd[0] == 'push':
#         op, num = cmd
#         a.append(int(num))
#         b.insert(0,int(num))
#     elif cmd[0] == 'pop':
#         if flag:
#             tmp = b.pop()
#             a.remove(tmp)
#             print(tmp)
#         else:
#             print(-1)
#     elif cmd[0] == 'size':
#         print(flag)
#     elif cmd[0] == 'empty':
#         print( 0 if flag else 1)
#     elif cmd[0] == 'front':
#         print(a[0] if flag else -1)
#     elif cmd[0] == 'back':
#         print(a[-1] if flag else -1)


import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])

for _ in range(n):
    cmd = list(input().split())
    flag = len(queue)

    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if flag:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(flag)
    elif cmd[0] == 'empty':
        print( 0 if flag else 1)
    elif cmd[0] == 'front':
        print(queue[0] if flag else -1)
    elif cmd[0] == 'back':
        print(queue[-1] if flag else -1)