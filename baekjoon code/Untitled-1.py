progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    ans = []
    
    while progresses:
        distribute = 0

        #작업률 업데이트
        progresses = [ p+s for p,s in zip(progresses,speeds)]
        
        #배포할 작업 업데이트 
        for p in progresses:
            if p >= 100:
                distribute += 1
            else: 
                break
            
        if distribute != 0:
                ans.append(distribute)
                progresses = progresses[distribute:]
                speeds = speeds[distribute:]
    return ans

print(solution(progresses,speeds))