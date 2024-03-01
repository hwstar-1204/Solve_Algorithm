#다리 만들기 
"""
dr,dc: 네 방향 탐색을 위한 상수 
n,m: 행렬의 크기 
mymap: 맵 정보 저장 리스트 
visited: BFS시 방문 여부 저장 리스트 

sNum: 섬 번호 
sumlist: 모든 섬 정보 이중 리스트 
mlist: 1개의 섬 정보 리스트 

addNode(i,j,queue): #섬 한칸을 더해주는 함수 
    mymap에서 i,j위치에 섬 번호 저장 
    해당 위치에 방문 표시 
    섬 정보(mlist)에 해당 노드 추가 
    BFS를 위한 큐에 해당 노드 추가 

BFS(i,j) #탐색을 통해 섬 정보를 저장 
    i,j 위치에서 네 방향으로 연결된 모든 노드를 탐색하여 1개의섬의 영역을 저장 
    연결된 새로운 노드가 확인되면 addNode를 통해 정보 저장 

for i~n만큼 반복:
    for j~m만큼 반복:
        BFS(i,j) #BFS실행하여 하나의 섬 정보를 가져오기 
        BFS 결과(하나의 섬 정보)를 sumlist에 추가 
        sNum의 값을 하나 증가 #새로운 섬 넘버링 

pq(우선순위 큐)

for sumlist크기만큼 반복: #모든 섬에서 지을 수 있는 다리 찾고 저장 
    now <- sumlist에서 추출
    for now 크기만큼 반복:
        1개의 섬의 모든 위치에서 만들 수 있는 다리 정보 저장 
        # 네 방향 탐색 -> 우선순위 큐에 에지 정보 저장 

union(a,b):

find(a):

parent: 대표노드 저장 리스트
useEdge: 사용한 에지 수 
result: 정답 변수 

while 큐가 빌때까지:
    큐에서 에지 정보 가져오기 
    if 에지 시작점과 끝점의 부모 노드가 다르면:
        union연산 수행 
        에지의 가중치를 정답 변수에 더하기 
        사용한 에지의 수 1 증가 

if 사용한 에지의 수가 노드 -1만큼이면:
    정답 변수 출력
else:
    -1 출력 
"""
import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

dr = [0,1,0,-1]
dc = [1,0,-1,0]

n,m = map(int,input().split())
mymap = [[0 for j in range(m)] for i in range(n)]
visited = [False for j in range(m) for i in range(n)]

for i in range(n):
    mymap[i] = list(map(int,input().split()))

sNum = 1
sumlist = list([])
mlist = []

def addNode(i,j,queue):
    mymap[i][j] = sNum
    visited[i][j] = True
    temp = [i,j]
    mlist.append(temp)
    queue.append(temp)

def BFS(i,j):
    queue = deque()
    mlist.clear()
    start = [i,j]
    queue.append(start)
    mlist.append(start)
    visited[i][j] = True
    mymap[i][j] = sNum

    while queue:
        r,c = queue.popleft()
        for d in range(4):
            tempR = dr[d]
            tempC = dr[d]
            while r+tempR >=0 and r+tempR < n and c+tempC>=0 and c+tempC <m:
                if not visited[r+tempR][c+tempC] and mymap[r+tempR][c+tempC] != 0:
                    addNode(r+tempR,c+tempC,queue)

                else:
                    break
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1
                elif tempC <0:
                    tempC -= 1
                elif tempC >0:
                    tempC += 1
    return mlist

for i in range(n):
    for j in range(m):
        if mymap[i][j] != 0 and not visited[i][j]:
            #깊은 복사로 해야 주소를 공유하지 않음 
            templist = copy.deepcopy(BFS(i,j))
            sNum += 1
            sumlist.apend(templist)

pq = PriorityQueue()

for now in sumlist:
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = mymap[r][c]
        for d in range(4):
            tempR = dr[d]
            tempC = dr[d]
            blength  = 0

            while r+tempR>=0 and r+tempR <n and c+tempC >=0 and c+tempC < m:
                if mymap[r+tempR][c+tempC] == now_S:
                    break
                #같은 섬도 아니고 바다도 아니면 
                elif mymap[r+tempR][c+tempC] != 0:
                    if blength >1:
                        pq.put((blength,now_S, mymap[r+tempR][c+tempC]))
                    break
                else: #바다이면 다리의 길이 연장
                    blength += 1
                if tempR <0:
                    tempR -= 1
                elif tempR >0:
                    tempR += 1
                elif tempC <0:
                    tempC -= 1
                elif tempC > 0:
                    tempC += 1


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

parent = [0]*sNum

for i in range(len(parent)):
    parent[i] = i 

useEdge = 0
result = 0

while pq.qsize >0:
    v,s,e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result += v
        useEdge += 1

if useEdge == sNum - 2:
    print(result)
else:
    print(-1)