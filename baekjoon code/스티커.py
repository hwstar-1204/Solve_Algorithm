#스티커
"""
50 60 100 50 20 
50 30  10 70 60 

100 70 50 60 = 280
70 100 50 20 = 240
60 100 50 30 = 240
///
50 60 100 50 20 
10 30  10 70 80 

100 80 50 30 = 260
80 100 50 30 = 260 
70 100 50 30 20 = 270 
///
50 10 100 20 40         전체합: 440
30 50 70 10 60 

50 - 상하좌우 + 나머지 값 = 전체 - 선택값 상하좌우값  
->>> 계선 : 전체 - (선택값+상하좌우값)을 저장 
(1)
50: 400 = 350     30: 340 = 310
10: 240 = 230    50: 330 = 280
100: 340 = 240    70: 280 = 210
20: 290 = 270   10: 290 = 280
40: 360 = 320    60: 390 = 330
(2)
50선택 -> 50과 주변값을 0으로 만듬, 전체값-=(50+50주변값)= 400-50, 정답+= 선택값(50)
전체값: 350
if 선택값: #0이 아니면
    그 자리에서 위와 같은 내용 반복 
100: 260 = 160
20: 200 = 180
40: 270 = 230
50: 280 = 230
70: 190 = 120
10: 200 = 190
60: 300 = 240
(3)
60 선택 
...
리스트 합이 0이면 반복 끝
"""

# import sys
# input = sys.stdin.readline
# tc = int(input())
# dx,dy = [0,1,0,-1], [-1,0,1,0] #하우상좌

# def del_sum(board,i,j):
#     tmp_del = []
#     tmp_del.append(board[i][j])
#     board[i][j] = 0

#     for t in range(4):
#         mx, my = dx[t]+i, dy[t]+j
#         if 0 <= mx < n and 0 <= my < 2: 
#             tmp_del.append(board[mx][my])
#             board[mx][my] = 0
#     return sum(tmp_del)


# for _ in range(tc):
#     del_list = [] # 보드에서 삭제된 요소
#     answer = [[0]*n for _ in range(2)]    # 선택한 값들 저장
#     total = 0     # 보드의 합
#     n = int(input())
#     board = [list(map(int,input().split())) for _ in range(2)]

#     while 2*n == len(del_list) + len(answer):

#         for i in range(2):
#             for j in range(n):
#                 if board[i][j]:
#                     answer[i][j] = total - del_sum(board,i,j)

        

#//-------------------------//
import sys
input = sys.stdin.readline
tc = int(input())
answer = []

for _ in range(tc):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(2)]
    if n == 1:
        answer.append(max(board[0][0],board[1][0]))
        continue
    board[0][1] += board[1][0]
    board[1][1] += board[0][0]
    for i in range(2,n):
        board[0][i] += max(board[1][i-2], board[1][i-1])
        board[1][i] += max(board[0][i-2], board[0][i-1])
    
    answer.append(max(board[0][n-1], board[1][n-1]))

print(*answer,sep='\n')

