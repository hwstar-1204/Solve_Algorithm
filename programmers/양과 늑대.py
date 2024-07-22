from collections import deque

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    max_sheep = 0
    q = deque([(0, 1, 0, set())])  # 현재 위치, 양, 늑대, 방문한 노드
    
    while q:
        now, sheep, wolf, visited = q.popleft()
        max_sheep = max(sheep, max_sheep)
        visited.update(tree[now])
        
        for next_node in visited:
            if info[next_node]:
                if sheep != wolf+1:
                    q.append(
                        (next_node, sheep, wolf+1, visited - {next_node})
                    )
            else:
                q.append(
                    (next_node, sheep+1, wolf, visited - {next_node})
                )
                
    return max_sheep