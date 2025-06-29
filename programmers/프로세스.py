from collections import deque

def solution(priorities, location):
    q = deque([(p,i) for i,p in enumerate(priorities)])  # 우선순위, index
    ans = 0    
    
    while q:
        now = q.popleft()
        if any(now[0] < p[0] for p in q):
            q.append(now)
            continue
        
        ans += 1
        if location == now[1]:
            return ans
        
