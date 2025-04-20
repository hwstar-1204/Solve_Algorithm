# Loop version
from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    all_courses = permutations(dungeons, len(dungeons))

    for course in all_courses:
        tmp_k = k # 60 20 
        tmp_cnt = 0 # 1 2
        for c in course:
            if c[0] <= tmp_k:
                tmp_k -= c[1]
                tmp_cnt += 1

        max_count = max(max_count, tmp_cnt)
        
    return max_count

# backtracking version 1
def solution(k, dungeons):
    n = len(dungeons)
    max_count = 0

    def backtrack(stamina, visited, count):
        nonlocal max_count
        max_count = max(max_count, count)

        for i in range(n):
            if not visited[i] and dungeons[i][0] <= stamina:
                visited[i] = True
                backtrack(stamina - dungeons[i][1], visited, count + 1)
                visited[i] = False
    
    visited = [False] * n
    backtrack(k, visited, 0)
    return max_count

# backtracking version 2
def solution(k, dungeons):
    ans = 0
    visited = [False] * len(dungeons)
    
    def backtrack(visited, now_k, count):
        nonlocal ans
        ans = max(ans, count)

        for i, (min_k, work_k) in enumerate(dungeons):
            if now_k < min_k or visited[i]:
                continue

            visited[i] = True
            backtrack(visited, now_k-work_k, count+1)
            visited[i] = False
            
    backtrack(visited, k, 0)
    return ans

# backtracking version 3
def solution2(k, dungeons):
    ans = 0
    
    def backtrack(remaining_dungeons, now_k, count):
        nonlocal ans
        ans = max(ans, count)

        for i, (min_k, work_k) in enumerate(remaining_dungeons):
            if now_k >= min_k:
                next_remaining = remaining_dungeons[:i] + remaining_dungeons[i+1:] 
                backtrack(next_remaining, now_k-work_k, count+1)
            
    backtrack(dungeons, k, 0)
    return ans
