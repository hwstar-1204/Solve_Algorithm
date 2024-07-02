"""
터진 인형 수 = 0
바구니 = stack

for moves:    
    물건뽑기 
        뽑은 위치 = 0
    
    if 뽑은 물건 == 바구니 맨 위:
        터진 인형 수 += 2
    else:
        바구니 맨 위에 뽑은 물건 넣기 
"""

def solution(board, moves):
    answer = 0
    bucket = []
    
    for x in moves:
        # 물건 뽑기 
        select = 0  # 뽑은 물건
        for y in range(len(board)):
            if board[y][x-1]:
                select = board[y][x-1]
                bucket.append(select)
                board[y][x-1] = 0
                break
        
        if len(bucket) > 1 and bucket[-2] == bucket[-1]:
            bucket.pop()
            bucket.pop()
            answer += 2

    return answer

# 최적화 풀이
def solution2(board, moves):
    answer = 0
    bucket = []

    length = len(board)
    top_idx = [0] * length

    # 초기 top index 설정
    for j in range(length):
        for i in range(length):
            if board[i][j]:
                top_idx[j] = i
                break

    for x in moves:
        col = x - 1
        if top_idx[col] < length:
            select = board[top_idx[col]][col]
            if select:
                board[top_idx[col]][col] = 0
                top_idx[col] += 1  # 다음 인형 위치로 이동
                
                if bucket and select == bucket[-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(select)
    
    return answer
