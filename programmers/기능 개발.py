import math 

def solution(progresses, speeds):
    answer = []
    complete_day = []
    n = len(progresses)
    
    for i in range(n):
        complete_day.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    first = complete_day[0]
    count = 0
    
    for i in range(n):
        if complete_day[i] <= first:
            count += 1
        else:
            answer.append(count)
            count = 1
            first = complete_day[i]
            
    answer.append(count)
    return answer
