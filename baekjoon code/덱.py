from collections import deque
import sys
input = sys.stdin.readline
dq = deque()
n = int(input())

for _ in range(n):
    cmd = list(input().split())
    s = len(dq)
    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print( dq.popleft() if s else -1)
    elif cmd[0] == 'pop_back':
        print( dq.pop() if s else -1)
    elif cmd[0] == 'size':
        print(s)
    elif cmd[0] == 'empty':
        print( 0 if s else 1)
    elif cmd[0] == 'front':
        print( dq[0] if s else -1)
    elif cmd[0] == 'back':
        print( dq[-1] if s else -1)