#위상 정렬 
"""
사이클이 없는 방향 그래프에서 노드 순서를 찾는 알고리즘 
시간복잡도: O(V+E)
항상 유일한 값으로 정렬되지 않음 

1. 진입차수(자기 자신을 가리키는 에지 개수) 리스트를 만듬 
그래프는 이차원 리스트로 구현 
2. 진입차수 리스트에서 0인 노들르 선택하고 선택된 노드를 정렬 시스트에 저장 
그 후 인접 리스트에서 선택된 노드가 가리키는 노드들의 진입 차수를 1씩 뺀다
계속해서 다음 노드를 선택하여 반복 (모든 노드가 정렬될때까지 반복 )
"""
#줄 세우기 
"""
n: 학생수
m: 비교 횟수
a: 비교 데이터 저장 인접 리스트 
indegree: 진입 차수 리스트 

for m만큼 반복:
    인접 리스트 데이터 저장
    진입 차수 리스트 초기 데이터 저장 

#위상정렬 수행
큐 생성

for n만큼 반복:
    진입 차수 리스트의 값이 0인 학생을 큐에 삽입 

while 큐가 빌때까지:
    현재 노드 = 큐에서 데이터 가져오기 
    현재 노드값 출력 
    for 현재 노드에서 갈 수 있는 노드의 개수:
        타깃 노드 진입 차수 리스트 값 1감소
        if 타깃 노드의 진입 차수가 0이면:
            큐에 타깃 노드 추가 
"""

from collections import deque
n,m = map(int,input().split())
a = [[]for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    s,e = map(int,input().split())
    a[s].append(e)
    indegree[e] += 1

queue = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end='')
    for next in a[now]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)