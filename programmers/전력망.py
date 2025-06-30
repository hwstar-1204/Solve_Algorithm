from collections import deque

def bfs(graph, visited, start):
    q = deque([start])
    cnt = 0
    
    while q:
        now = q.popleft()
        visited[now] = True
        cnt += 1
        for nxt in graph[now]:
            if not visited[nxt]:
                q.append(nxt)
    
    return cnt

def dfs(graph, visited, start):
    visited[start] = 1    
    cnt = 1

    for next_node in graph[start]:
        if not visited[next_node]:
            cnt += dfs(graph, visited, next_node)
    return cnt
            

def solution(n, wires):
    ans = n
    for i in range(len(wires)):
        cut_wires = wires[:i] + wires[i+1:]
        
        visited = [False for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]
        for v1,v2 in cut_wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        # cnt = bfs(graph, visited, 1)
        cnt = dfs(graph, visited, 1)
        diff = abs(2*cnt - n)
        ans = min(ans, diff)

    return ans
