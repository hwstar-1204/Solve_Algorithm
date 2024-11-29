"""
가장 많이 연결된 노드에 연결된 전선을 하나씩 끊어보면서 가장 비슷하게 송전탑을 가지고 있는 경우의 차이수를 반환 
1. 그래프로 표현
2. 가장 많은 전선을 가진 송전탑 선택
3. 해당 송전탑에 연결된 전선을 끊고 개수 세기 
4. 차이 계산하기 
5. 최소일 경우 정답 업데이트 
"""


from collections import deque        

def solution(n, wires):
    min_diff = float('inf')
    graph = [[] for _ in range(n+1)]
    
    for s, e in wires:
        tuning_graph(graph, s, e, True)
    
    for s, e in wires:
        tuning_graph(graph, s, e, False)

        count1 = bfs(graph, s, n)
        count2 = n - count1        
        min_diff = min(min_diff, abs(count1 - count2))

        tuning_graph(graph, s, e, True)

    return min_diff

def bfs(graph, s, n):
    queue = deque([s])
    visited = [False] * (n+1)
    visited[s] = True
    node_count = 1

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                node_count += 1
    
    return node_count

def tuning_graph(graph, s, e, is_connect):
    if is_connect:
        graph[s].append(e)
        graph[e].append(s)
    else:
        graph[s].remove(e)
        graph[e].remove(s)

    return graph


n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	
result = solution(n, wires)
print(result)
assert result == 1