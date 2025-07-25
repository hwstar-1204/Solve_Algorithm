def solution(targets):
    targets.sort(key=lambda x: x[1])
    ans = 0
    trigger = -1
    
    for s,e in targets:
        if trigger <= s:
            ans += 1
            trigger = e
    return ans
