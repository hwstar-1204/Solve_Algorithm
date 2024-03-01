#세일즈맨의 고민 
"""
n:노드 개수 , m: 에지 개수
scity: 시작 도시, ecity: 도착 도시 
edges: 에지 리스트 
distnace: 거리 리스트 

for 에지 개수만큼 반복:
    에지 리스트에 에지 정보 저장 

cityMoney: 각 도시에서 버는 수입 저장 

#변형된 밸먼 포드 수행 
거리 리스트에 출발 노드 citymoney[출발노드]로 초기화 

for 노드 개수 + 100만큼 반복:
    for 에지 개수만큼 반복:
        현재 에지 데이터 가져오기 
        if 출발 노드가 방문하지 않은 노드:
            skip
        elif 출발노드가 양수 사이클에 연결된 노드:
            종료 노드를 양수 사이클에 연결된 노드로 업데이트 
        elif 종료 노드의 값 < 출발 노드의 값 + 도착 도시에서의 수입 - 에지의 가중치 :
            # 더많은 수입을 얻는 경로가 새로 발견될때 
            종료 노드의 값을 업데이트 
            if 노드 개수 -1 반복 이후 업데이트:
                종료 노드를 양수 사이클 연결 노드로 업데이트 

#도착 도시의 값에 따른 결과 출력 
도착 도시가 초깃값이면 도착 불가 -> gg
도착 도시가 양수 사이클이면 돈을 무한대로 벌ㅇ므 -> Gee
이외의 경우는 도착 도시의 값 출력 
"""
import sys
input = sys.stdin.readline
n,scity,ecity,m = map(int,input().split())
edges = []
distance = [-sys.maxsize]*n

for _ in range(m):
    start,end,price = map(int,input().split())
    edges.append((start,end,price))

citymoney = list(map(int,input().split()))

#변형된 밸만 포드 수행 
distance[scity] = citymoney[scity]

for i in range(n+101):
    for start,end,price in edges:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + citymoney[end] - price:
            distance[end] = distance[start] + citymoney[end] - price
            if i > n-1:
                distance[end] = sys.maxsize

if distance[ecity] == -sys.maxsize:
    print("gg")
elif distance[ecity] == sys.maxsize:
    print("Gee")
else:
    print(distance[ecity])