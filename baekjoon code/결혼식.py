"""
n : 동기 수  (2 <= n <= 500)
m : 친구 관계 수 (1 <= m <= 10000)

BFS
"""

import sys
from collections import deque
input = sys.stdin.readline

# v1
# n = int(input())
# m = int(input())
# ans, lv = 0, 0

# relations = [[] for _ in range(n+1)]
# visited = [False] * (n+1)

# for _ in range(m):
#     r1, r2 = map(int, input().split())
#     relations[r1].append(r2)
#     relations[r2].append(r1)

# q = deque([1])
# visited[1] = True


# while q:
#     if lv == 2:
#         break

#     for _ in range(len(q)):
#         node = q.popleft()
#         for r in relations[node]:
#             if not visited[r]:
#                 ans += 1
#                 q.append(r)
#                 visited[r] = True

    # lv += 1

# print(ans)

##########################################

# v2
import sys
from collections import deque
input = sys.stdin.readline

n, m = int(input()), int(input())
relations = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    r1, r2 = map(int, input().split())
    relations[r1].append(r2)
    relations[r2].append(r1)

q = deque([1])
visited[1] = 1

while q:
    node = q.popleft()
    for r in relations[node]:
        if not visited[r]:
            q.append(r)
            visited[r] = visited[node] + 1

ans = sum([1 for level in visited if 1 < level <= 3])
print(ans)