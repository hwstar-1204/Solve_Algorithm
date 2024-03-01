#임계 경로 구하기 
"""
n: 도시 수 
m: 도로 수
a: 도시 인접 리스트 
reverseA: 역방향 인접 리스트 
indegree: 진입 차수 리스트 

for m:
    인접 리스트 데이터 저장
    역방향 인접 리스트 데이터 저장 
    진입 차수 리스트 저장 

시작 도시 도착 도시 데이터 받기 

#위상정렬 수행 
큐 생성
출발 도시를 큐에 삽입 
result(결괏값)

while 큐가 빌떄까지:
    현재 노드 = 큐에서 데이터 가져오기 
    for 현재 노드에서 갈 수 있는 노드 탐색:
        타깃 노드 진입 차수 리스트 1감소
        result = 타깃 노드의 현재 경롯값과  현재 노드의 경롯값+도로 시간값 중 큰 값으로 저장 
        if 타깃 노드의 진입 차수 == 0:
            큐에 타깃 노드 추가 

resultCount(1분도 쉬지 않고 달려야하는 도로의 수 )
visited : 각도시의 방문 유무 저장 
도착 도시를 큐에 삽입
visited 리스트에 도착 도시를 방문 도시로 표시 

#위상 정렬 역방향 수행 
while 큐가 빌때까지:
    현재 노드 = 큐에서 데이터 가져오기 
    for 현재 노드에서 갈 수 잇는 노드의 개수:
        if 타깃 노드의 result값 + 도로를 걸리는데 지나는 시간  == 현재 노드의 result 값
            1분도 쉬지않고 달려야 하는 도로의 값 1증가 
            if 아직 방문하지 않은 도시:
                visited 리스트에 방문 도시 표시 
                큐에 타깃 노드 추가 

만나는 시간 (result[enddosi]) 출력
1분도 쉬지 않고 달려야 하는 도로의 수 resultCount 출력 
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
reverseA = [[] for _ in range(n+1)]
indegree = [0] *(n+1)

for i in range(m):
    s,e,v = map(int,input().split())
    a[s].append((e,v))
    reverseA[e].append((s,v))
    indegree[i] += 1

startDosi,endDosi = map(int,input().split())

queue = deque()
queue.append(startDosi)
result = [0] *(n+1)

while queue:
    now = queue.popleft()
    for next in a[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]],result[now]+next[1])
        if indegree == 0:
            queue.append(next[0])

resultCount = 0
visited = [False] * (n+1)
queue.clear()
queue.append(endDosi)
visited[endDosi] = True

while queue:
    now = queue.popleft()
    for next in reverseA[now]:
        if result[next[0]] + next[1] == result[now]:
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[endDosi])
print(resultCount)