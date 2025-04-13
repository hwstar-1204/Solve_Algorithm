def solution(n,wires):
    def dfs(node, visited, graph):
        visited[node] = True
        count = 1
        for next_node in graph[node]:
            if not visited[next_node]:
                count += dfs(next_node, visited, graph)
        return count
    
    min_diff = n
    
    for i in range(len(wires)):
        tmp_wires = wires[:i] + wires[i+1:]

        graph = [[] for _ in range(n+1)]
        visited = [False] * (n+1)

        for a,b in tmp_wires:
            graph[a].append(b)
            graph[b].append(a)

        cnt = dfs(1, visited, graph)
        diff = abs(n - cnt - cnt)
        min_diff = min(min_diff, diff)

    return min_diff
