#미로 탐색하기 
"""
dx, dy : 상하좌우를 탐색하기 위한 define값 정의 변수 
n: row, m: col
a: 데이터 저장 2차원 행렬
visited: 방문 기록 저장 리스트 

for n만큼 반복: 
    for m만큼 반복:
        a 리스트에 데이터 저장 

#BFS 구현하기 
BFS:
    큐에 시작 노드 삽입 
    visited 리스트에 현재 노드 방문 기록 
    while 큐가 빌떄까지:
        큐에서 노드 데이터 가져오기 
        for 상하좌우 탐색:
            if 유효한 좌표:
                if 이동할 수 있는 칸이면서 방문하지 않은 노드:
                visited 리스트에 방문 기록
                a리스트에 depth를 현재 노드의 depth+1 로 업데이트 
                큐에 데이터 삽입 

BFS(0,0) 실행 
a[n-1][m-1] 출력 
"""

from collections import deque
#상하좌우 탐색하기 위한 리스트 선언 
dx = [0,1,0,-1]
dy = [1,0,-1,0]
n,m = map(int,input().split())
a = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    numbers = list(input())
    for j in range(m):
        a[i][j] = int(numbers[j])

def BFS(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<n and y<m:
                if a[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    a[x][y] = a[now[0]][now[1]]+1
                    queue.append((x,y))
BFS(0,0)
print(a[n-1][m-1])