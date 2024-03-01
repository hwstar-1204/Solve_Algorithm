#게임 개발하기 
"""
n: 건물 수 
a: 건물 데이터 저장 인접 리스트 
indegree: 진입 차수 리스트 
selfbuild: 자기 자신을 짓는데 걸리는 시간 저장 리스트 

for n:
    인접 리스트 데이터 저장 
    진입 차수 리스트 저장 
    자기 자신 시간 리스트 데이터 저장 

#위상정렬 수행
큐 생성 

for n만큼 반복:
    진입 차수 리스트의 값이 0인 건물(노드)를 큐에 삽입 

while 큐가 빌때까지:
    현재 노드 = 큐에서 데이터 가져오기 
    for 현재 노드에서 갈 수 있는 노드 탐색 
        타깃 노드 진입 차수 리스트 1 감소
        결과 노드 업데이트 = max(현재 저장된 값, 현재 출발 노드+비용)
        if 타깃노드의 진입 차수가 0이면:
            우선순위 큐에 타깃 노드 추가 

위상 정렬 결과 출력 
"""
from collections import deque

n = int(input())
a = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
selfbuild = [0] * (n+1)

for i in range(1,n+1):
    inputlist = list(map(int,input().split()))
    selfbuild[i] = inputlist[0]
    index = 1
    while True:
        pretemp = inputlist[index]
        index += 1
        if pretemp == -1:
            break
        a[pretemp].append(i)
        indegree[i] += 1

queue = deque()

for i in range(n):
    if indegree[i] == 0:
        queue.append(i)

result = [0]*(n+1)

while queue:
    now = queue.popleft()
    for next in a[now]:
       indegree[next] -= 1
       result[next] = max(result[next],result[now]+selfbuild[now]) 
       if indegree[next] == 0:
           queue.append(next)

for i in range(1,n+1):
    print(result[i]+selfbuild[i])