def solution(citations):
    citations.sort()
    answer = []
    for i in range(len(citations)):
        up = 0
        down = 0
        for c in citations:
            if c < citations[i]:
                down += 1
            elif c >citations[i]:
                up += 1
            else:
                down += 1
                up += 1    
        if down == up:
            answer.append(citations[i])
    return max(answer)
            

c = [3, 0, 6, 1, 5]
print(solution(c))