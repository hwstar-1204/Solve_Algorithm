#최소 비용 구하기 
from queue import PriorityQueue
import sys
input = sys.stdin.readline
v = int(input())
e = int(input())

a = [[] for _ in range(v+1)] #비용 인접 리스트
visited = [False] * (v+1) #방문 여부 리스트
distance = [sys.maxsize] * (v+1) #거리 저장 리스트 

for i in range(e):
    s,e,w = map(int,input().split())
    a[s].append((e,w))

def minDistance(start,end):
    queue = PriorityQueue() 
    queue.put((0,start)) #가중치,시작점 형태로 
    distance[start] = 0 ## mistake 시작점 거리 초기화 

    while queue.qsize() > 0:
        now = queue.get()
        now_v = now[1] #현재 방문 노드 번호 
        if not visited[now_v]:
            visited[now_v] = True
            for node in a[now_v]: #받을때는 그냥 초기화했을때 자리 그대로 가져오기만 하면됨 
                next = node[0]  #다음 방문 노드 번호
                value = node[1] #현재 노드부터 다음 방문 노드 가중치 
                if not visited[next] and distance[next] > distance[now_v] + value:
                    distance[next] = distance[now_v] + value
                    queue.put((distance[next],next)) #우선순위 큐에 넣을때는 거꾸로 넣는거만 조심 !!!
    return distance[end]


S,E = map(int,input().split()) #시작점,종료점

result = minDistance(S,E) #다익스트라 수행
print(result)  #종료점까지의 최소 거리 출력 