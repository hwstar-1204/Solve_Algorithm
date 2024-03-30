#강의실 배정 

import sys
import heapq
input = sys.stdin.readline

n = int(input())
cls_time = [0] * n
cls_time = [tuple(map(int, input().split())) for _ in range(n)] # start, terminate
cls_time.sort(key=lambda x: (x[0],x[1]))

heap_room = [cls_time[0][1]]
for s,t in cls_time[1:]:
    if heap_room[0] <= s:        # 지금까지 가장 빨리 끝나는 강의 <= 현재 강의 시작 시간
        heapq.heappop(heap_room) # 교체 
    heapq.heappush(heap_room,t)  # 기준점 추가 

print(len(heap_room))