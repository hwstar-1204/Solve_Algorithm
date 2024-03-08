#색종이 만들기 

"""
88

0
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [ list(map(int,input().split())) for _ in range(n)]
answer = []

def div_board(x,y,n):
    first_c = board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j] != first_c:
                div_board(x,y,n//2)
                div_board(x,y+n//2,n//2)
                div_board(x+n//2,y,n//2)
                div_board(x+n//2,y+n//2,n//2)
                return
    if first_c == 0:
        answer.append(0)
    else:
        answer.append(1)

div_board(0,0,n)
print(answer.count(0),answer.count(1),sep='\n')