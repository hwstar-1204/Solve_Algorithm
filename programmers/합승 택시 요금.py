import heapq 

def dijkstra(graph, start):
    distance = [float('inf')] * (len(graph)+1)
    distance[start] = 0

    queue = [(0, start)]
    heapq.heapify(queue)

    while queue:
        weight, end = heapq.heappop(queue)

        if distance[end] < weight: continue

        for w, e in graph[end]:
            if distance[e] > weight + w:
                distance[e] = weight + w
                heapq.heappush(queue, (weight + w, e))

    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for start, end, weight in fares:
        graph[start].append((weight, end))
        graph[end].append((weight, start))

    answers = []
    for i in range(1, n+1):
        # (s -> i) + {(i -> a) + (i -> b)}
        result = dijkstra(graph, s)[i] + dijkstra(graph, i)[a] + dijkstra(graph, i)[b]
        answers.append(result)

    return min(answers)


    
    
    

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(6,4,6,2,fares))