"""
모든 음식의 스코빌 지수르 k이상으로 만들어야함 
새로운 음식 스코빌 지수 = 1번째 작은 지수 + 2번째 작은 지수 * 2
2개 삭제 후 새로운거 삽입 

Heap 사용
특정 조건내에서 반복
- 최소값을 찾기 - O(1)
- 삽입, 삭제 - (logN)
"""
from heapq import heapify, heappop, heappush


def solution(scoville, K):
    cnt = 0  # 섞은 횟수 
    heapify(scoville)
    
    while len(scoville) >= 2:
        ms1 = heappop(scoville)
        if ms1 >= K:
            return cnt
        
        ms2 = heappop(scoville)
        heappush(scoville, ms1 + 2 * ms2)
        cnt += 1

    if scoville[0] >= K:
        return cnt
    return -1
