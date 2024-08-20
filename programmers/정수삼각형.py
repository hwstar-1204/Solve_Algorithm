# ver 1 (top down)
import copy

def solution(triangle):
    dp = copy.deepcopy(triangle)
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            if dp[i+1][j] < dp[i][j] + triangle[i+1][j]:
                dp[i+1][j] = dp[i][j] + triangle[i+1][j]
            if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]:
                dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
                
    return max(dp[-1])


# ver 2 (bottom up)
def solution(triangle):
    # 삼각형을 아래에서 위로 올라가면서 최대값을 계산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 바로 아래 줄의 두 값을 비교하여 더 큰 값을 현재 위치에 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    return triangle[0][0]