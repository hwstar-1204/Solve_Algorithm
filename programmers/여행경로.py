from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for s, e in tickets:
        graph[s].append(e)
        
    graph = {k: sorted(v) for k, v in graph.items()}
    
    stack = ['ICN']
    while stack:
        current = stack[-1]  # 현재 공항
        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(graph[current].pop(0))  # 다음 공항

    return answer[::-1]  # 역순으로 반환