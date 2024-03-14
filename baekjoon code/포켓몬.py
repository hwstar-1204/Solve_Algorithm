#포켓몬

"""
n: 도감에 수록되있는 포켓몬 수 
m: 내가 맞춰야 하는 문제의 개수 

1번~n번 포켓몬 한줄씩

숫자이면 포켓몬 이름
포켓몬이름이면 숫자 

반드시 있는 포켓몬만 물어봄
"""
# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# pocket = {}
# answer = []

# for i in range(1,n+1):
#     pocket[i] = input().rstrip()

# for i in range(m):
#     question = input().rstrip()
#     if question.isdigit():
#             answer.append(pocket[int(question)])
#     else: 
#         for key, value in pocket.items():
#             if question == value:
#                 answer.append(key)
# print(*answer,sep='\n')

#/-------------------------------------------------/
#/-------------------------------------------------/

# import sys
# input = sys.stdin.readline

# n,m = map(int,input().split())
# pocket = [input().rstrip() for _ in range(n)]
# answer = []

# for _ in range(m):
#     question = input().rstrip()
#     if question.isdigit():
#         print(pocket[int(question)-1])
#     else:
#         print(pocket.index(question)+1)

#/-------------------------------------------------/
#/-------------------------------------------------/

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
pocket = {}
answer = []

for i in range(1,n+1):
    mon = input().rstrip()
    pocket[i] = mon
    pocket[mon] = i

for i in range(m):
    question = input().rstrip()
    if question.isdigit(): # 숫자
        answer.append(pocket[int(question)])
    else: # 문자
        answer.append(pocket[question])
print(*answer,sep='\n')