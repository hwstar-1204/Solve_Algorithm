"""
n : 미로의 가로 크기  (1 <= n <= 1000)
미로에 적힌 숫자만큼 점프 가능 
왼쪽에서 오른쪽으로 최소로 점프해서 끝까지 갈 수 있는지, 없으면 -1
"""

from collections import deque
n = int(input())
miro = list(map(int,input().split()))

visited = [float('inf') for _ in range(n)]
visited[0] = 0

q = deque([(0, miro[0])])  # 현위치, 현재 점프 가능 수
while q:
    now_kan, can_jumps = q.popleft()
    for i in range(1, can_jumps+1):
        next_kan = now_kan + i
        if next_kan < n and visited[next_kan] > visited[now_kan] + 1:
            visited[next_kan] = visited[now_kan] + 1
            q.append((next_kan, miro[next_kan]))

print(visited[n-1] if visited[n-1] != float("inf") else -1)
