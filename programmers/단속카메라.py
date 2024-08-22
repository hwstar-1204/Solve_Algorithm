def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 1
    max = routes[0][1]
    
    for s,e in routes:
        if max < s:
            max = e
            answer += 1
            
    return answer
