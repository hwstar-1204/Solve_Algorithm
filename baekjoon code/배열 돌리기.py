import sys
import copy
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,d = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]
    tmp_array = copy.deepcopy(array)

    d = d if d >= 0 else d + 360

    for turn in range(d//45):
        for i in range(n):
            for j in range(n):
                if i == j:  # 주 대각선
                    tmp_array[i][j] = array[n//2][j]
                elif i == n//2: # 가운데 행
                    tmp_array[i][j] = array[n-j-1][j]
                elif i+j == n-1: # 부 대각선
                    tmp_array[i][j] = array[i][n//2]
                elif j == n//2: # 가운데 열
                    tmp_array[i][j] = array[i][i]
                else:  # 변하지 않는 부분
                    tmp_array[i][j] = array[i][j]

        array = copy.deepcopy(tmp_array)

    for a in array:
        print(*a)


"""
t = 5 (테스트 케이스 개수)
X = 5 (2차원 배열 크기)
d = 45 (각도, 방향)

(3,1) -> (1,1)
(3,2) -> (2,2)
(3,3) -> (3,3)  
(3,4) -> (4,4)
(3,5) -> (5,5)
=> (X//2, m) -> (m, m)

(1,1) -> (1,3)
(2,2) -> (2,3)
(3,3) -> (3,3)  
(4,4) -> (4,3)
(5,5) -> (5,3)
=> (n, m) -> (n, X//2)

(1,3) -> (1,5)
(2,3) -> (2,5)
(3,3) -> (3,3)
(4,3) -> (4,5)
(5,3) -> (5,5)
=> (n, X//2) -> (n, X) 

(1,5) -> (3,5)
(2,4) -> (3,4)
(3,3) -> (3,3)  
(4,2) -> (3,2)
(5,1) -> (3,1)
=> (n, X) -> (X//2, X)

for _ in range(테스트 케이스 개수):
    for _ in range(각도//45):
        for 1 ~ 5 (X//2 X)

시간복잡도 = 테캐(10) * 각도(8) * 배열크기(499)
"""

# import sys
# import copy
# input = sys.stdin.readline

# t = int(input())
# answer = []
# for _ in range(t):
#     n,d = map(int,input().split())
#     array = [[0]*(n+1)] + [[0] + list(map(int,input().split())) for _ in range(n)]
#     tmp_array = copy.deepcopy(array)

#     d = d if d >= 0 else d + 360

#     for turn in range(d//45):
#         for i in range(1, (n+1)//2):

#             tmp_array[i][i] = array[(n + 1) // 2][i]
#             tmp_array[i][(n + 1) // 2] = array[i][i]
#             tmp_array[i][n - i + 1] = array[i][(n + 1) // 2]
#             tmp_array[(n + 1) // 2][n - i + 1] = array[i][n - i + 1]
#             tmp_array[n - i + 1][n - i + 1] = array[(n + 1) // 2][n - i + 1]
#             tmp_array[n - i + 1][(n + 1) // 2] = array[n - i + 1][n - i + 1]
#             tmp_array[n - i + 1][i] = array[n - i + 1][(n + 1) // 2]
#             tmp_array[(n + 1) // 2][i] = array[n - i + 1][i]
            

#             # tmp_array[i][i] = array[(n+1)//2][i]
#             # tmp_array[i][(n+1)//2] = array[i][i]
#             # tmp_array[i][n] = array[i][(n+1)//2]  VV
#             # tmp_array[(n+1)//2][n-i+1] = array[i][n]
#             # tmp_array[n-i+1][n-i+1] = array[(n+1)//2][n-i+1]
#             # tmp_array[n-i+1][(n+1)//2] = array[n-i+1][n-i+1]
#             # tmp_array[n-i+1][n-i+1] = array[n-i+1][(n+1)//2]  VV
#             # tmp_array[(n+1)//2][i] = array[n-i+1][n-i+1]
            

#         array = copy.deepcopy(tmp_array)

#         if turn == d//45-1:
#             answer += array[1:]

# for a in answer:
#     print(*a[1:])

# ===============================================
