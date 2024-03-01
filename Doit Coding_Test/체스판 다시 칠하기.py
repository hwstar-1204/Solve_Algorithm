#체스판 다시 칠하기 
"""
보드판 입력받기 
체스판 8*8 초기화 
정답 리스트 초기화 

세로로 한칸씩 이동  #초기 색 저장 
가로로 한칸씩 이동  #이동할때 초기 색깔 번갈아가며

왼쪽 상단 8*8 체스판 입력받으면서 
왼쪽 상단이 흰색인지 검은색인지에 따라 조건 

가로로 이동할때는 큐에서 모든 0번째 행 삭제 + 다음 데이터 마지막행에 추가 

bw가 번갈아가면서 나오는지 확인 
번갈아 가면서 나오지 않는부분은 +1


정답 리스트 중 가장 작은 값 출력 
"""

# answer = [] #정답리스트 
# row,col = map(int,input().split())
# board = [input() for _ in range(row)] #보드판 입력 



# for i in range(row-7):#세로 이동
#     for j in range(col-7): #가로 이동 
#         chess = [board[x][j:j+8] for x in range(i, i+8)] #mistake
#         EvenC = chess[0][0] #짝수
#         OddC = 'W' if EvenC == 'B' else 'B' #홀수
#         tmp = 0  #한번 반복시 저장할 정답 데이터
#         #짝수행은 EvenC색, 홀수행은 EvenC와 다른색 
#         for ci in chess:
#             for cj,color in enumerate(ci):
#                 if cj%2 == 0 and color != EvenC:# 짝수칸인데 다른색
#                     tmp += 1
#                 if cj%2 == 1 and color != OddC:# 홀수칸인데 처음색 
#                     tmp += 1
#             EvenC = OddC
#             OddC = 'W' if EvenC == 'B' else 'B'
#         answer.append(tmp)

# print(min(answer))
import sys
input = sys.stdin.readline
answer = []  # 정답 리스트
row, col = map(int, input().split())
board = [input() for _ in range(row)]  # 보드판 입력

for i in range(row - 7):  # 세로 이동
    for j in range(col - 7):  # 가로 이동
        chess = [board[x][j:j+8] for x in range(i, i+8)]
        EvenC = chess[0][0]  # 짝수색
        OddC = 'W' if EvenC == 'B' else 'B'  # 홀수색
        tmp1 = 0  # 맨 왼쪽 위가 W일 때의 정답 데이터
        tmp2 = 0  # 맨 왼쪽 위가 B일 때의 정답 데이터

        # 짝수행은 EvenC색, 홀수행은 EvenC와 다른 색
        for ci in chess:
            for cj, color in enumerate(ci):
                if cj % 2 == 0 and color != EvenC:  # 짝수칸인데 짝수색
                    tmp1 += 1
                if cj % 2 == 1 and color != OddC:  # 홀수칸인데 홀수색
                    tmp1 += 1
                if cj % 2 == 0 and color != OddC:  # 짝수칸인데 짝수색
                    tmp2 += 1
                if cj % 2 == 1 and color != EvenC:  # 홀수칸인데 홀수색
                    tmp2 += 1
            EvenC = OddC
            OddC = 'W' if EvenC == 'B' else 'B'
        
        answer.append(min(tmp1, tmp2)) #처음색이 흰색이었을때와 짝수이었을때 최소로 바꾸는 개수

print(min(answer))
