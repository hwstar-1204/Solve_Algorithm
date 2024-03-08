# 빙고
import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(5)]
row = [[] for _ in range(5)] # 가로
col = [[] for _ in range(5)] # 세로
cross = [[]*2] #left right
binggo = 0

def search_check_num(board,row,col,cross,target):
    for i in range(5):
        for j in range(5):
            if board[i][j] == target:
                row[i].append(target)
                col[4-j].append(target)
                if i == j:
                    cross[0].append(target)
                elif i+j == 4:
                    cross[1].append(target)


def check_binggo(row,col,binggo):
    for r,c in zip(row,col):
        if len(r) == 5:
            binggo += 1
        if len(c) == 5:
            binggo += 1
        if

        if binggo >= 3:
            print(cnt+j)
            break       

for i in range(5):
    cnt = 1
    voice = list(map(int,input().split()))
    
    # 부른숫자 보드에서 찾아서 0 체크 
    for j, target in enumerate(voice):
        search_check_num(board,row,col,cross,target)
        # 만약 빙고면 빙고 개수 추가
        check_binggo(row,col,binggo)
        # 만약 빙고가 3개이면 끝 
        
    print("row,col 시작")
    print(row,"\n")
    print(col)
    cnt += 5