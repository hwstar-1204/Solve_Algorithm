import heapq


def solution(n, works):
    if n >= sum(works):
        return 0
    
    heap = [-w for w in works]
    heapq.heapify(heap)

    while heap:
        if not n or not heap[0]:
            break
        n -= 1
        max_work = heapq.heappop(heap)
        heapq.heappush(heap, max_work+1)

    return sum([w**2 for w in heap])