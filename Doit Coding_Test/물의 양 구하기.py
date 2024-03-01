#물의 양 구하기 
"""
sender, receiver : 6가지 경우를 탐색하기 위한 리스트 
now: a,b,c의 값 저장 
visited: 방문 여부 저장 리스트 
answer: 정답 리스트 

#BFS:
    큐 자료구조에 출발 노드 더하기 -> a,b가 0인 상태이므로 0,0 노드에서 시작하기
    visited 리스트에 현재 노드 방문 기록
    answer 리스트에 현재 C의 값 체크 
    while 큐가 빌때까지:
        큐에서 노드 데이터 가져오기 
        데이터를 이용해 a,b,c의 값 초기화 
        for 6가지 케이스 반복:
            받는 물통에 보내려는 물통의 값 더하기 
            보내려는 물통의 값을 0으로 업데이트하기 
            if 받는 물통이 넘칠때:
                넘치는 만큼 보내는 물통에 다시 넣어 주고받는 물통은 이 물통의 최댓값으로 저장 
            if 현재 노드의 연결 노드 중 방문하지 않은 노드:
                큐에 데이터 삽입
                visited 리스트에 방문 기록 
                if 1번째 물통이 비어있을 때:
                    3번째 물통의 양을 answer리스트에 기록

BFS 수행 

for answer 리스트 탐색:
    answer 리스트에서 값이 true인 index를 정답으로 출력 
"""
from collections import deque
#두 리스트를 이용하여 6가지 이동 케이스를 간편하게 정의할 수 있다. 
#여기에서 0,1,2는 각각 a,b,c 물통을 뜻한다. 
#ex) index=0 인 경우 sender[0]:0, reciever[0]:1 이기 때문에
# a->b 케이스를 뜻한다. 

sender = [0,0,1,1,2,2]
receiver = [1,2,0,2,0,1]
now = list(map(int,input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    answer[now[2]] = True

    while queue:
        print("ing")
        now_node = queue.popleft()
        a = now_node[0]
        b = now_node[1]
        c = now[2] -a-b #c는 전체 물의 양에서 a와b를 뺀 것 
        for k in range(6):
            next = [a,b,c]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > now[receiver[k]]: #물이 넘칠때
                #초과한 만큼 다시 이전 물통에 넣어주기 
                next[sender[k]] = next[receiver[k]]-now[receiver[k]]
                next[receiver[k]] = now[receiver[k]] # 대상 물통 최대로 채우기 
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] == 0:
                    answer[now[2]] = True

BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i,end='')

