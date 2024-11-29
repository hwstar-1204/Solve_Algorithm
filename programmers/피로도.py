"""
최소 필요 피로도 >= 소모 피로도 
던전을 최대한 많이 탐험

k : 유저 피로도 
dungeons : 던전별 [최소 필요 피로도, 소요 피로도]

return 탐험 최대 던전 수 
--

dungeons 정렬 (최소 필요도가 큰 순서 , 소모 피로도가 작은 순서 )
최소 필요도 - 소모피로도 가 큰 순서 라는거와 같은 이치 

sudo code
# 던전 입장
for d in dungeons
    # 던전 조건 확인 
    if 최소 피로도 <= 현재 피로도 
        # 피로도 계산 
        현재 피로도 - 소모 피로도 
        # 던전 입장수 + 1
        count += 1
"""
# Loop version
from itertools import permutations

def solution(k, dungeons):
    max_count = 0
    
    all_courses = permutations(dungeons, len(dungeons))
    print(*all_courses)

    for course in all_courses:
        tmp_k = k # 60 20 
        tmp_cnt = 0 # 1 2
        for c in course:
            if c[0] <= tmp_k:
                tmp_k -= c[1]
                tmp_cnt += 1

        max_count = max(max_count, tmp_cnt)
        if max_count == tmp_cnt:
            print(c)
        
    return max_count

# backtracking version
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


dungeons = [[80,20],[50,40],[30,10]]	
# dungeons = [[80,20],[50,40],[30,10],[40,20]]
k = 80

result = solution(k, dungeons) # 3
assert result == 3