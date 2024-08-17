"""
map = (m+1)*(n+1) 안에는 모두 0으로 초기화 
(1,1) 지점은 1로 초기화 
위쪽부터 차례대로 최소 경로수 계산
    웅덩이 위치는 pass
    다음 최소 경로수 = 왼쪽 최소경로수 + 위쪽 최소경로수

return map[n][m] % 1000000007

"""

def solution(m, n, puddles):
    maps = [[0]*(m+1) for _ in range(n+1)]
    maps[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                continue
            maps[i][j] += maps[i-1][j] + maps[i][j-1]

    return maps[n][m] % 1000000007