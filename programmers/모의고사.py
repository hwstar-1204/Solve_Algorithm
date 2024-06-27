def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    max_list = [0] * 3 
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                max_list[j] += 1
                
    max_score = max(max_list)
    highest = []
    
    for i, score in enumerate(max_list):
        if max_score == score:
            highest.append(i+1)
            
    return highest
            