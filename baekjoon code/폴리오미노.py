#폴리오미노

# board = list(input())
# idx = 0
# answer = True
# while idx < len(board):
#     if board[idx:idx+4] == 'XXXX':
#         board[idx:idx+4] = 'AAAA'
#         idx += 4
#     elif board[idx:idx+2] == 'XX':
#         board[idx:idx+2] = 'BB'
#         idx += 2
#     elif board[idx] == 'X':
#         answer = False
#         break
#     elif board[idx] == '.':
#         board[idx] = '.'
#         idx += 1

# print(board if answer else -1)

board = list(input())
idx = 0
answer = True
while idx < len(board):
    if board[idx:idx+4] == ['X', 'X', 'X', 'X']:
        board[idx:idx+4] = ['A', 'A', 'A', 'A']
        idx += 4
    elif board[idx:idx+2] == ['X', 'X']:
        board[idx:idx+2] = ['B', 'B']
        idx += 2
    elif board[idx] == 'X':
        answer = False
        break
    elif board[idx] == '.':
        board[idx] = '.'
        idx += 1

print(''.join(board) if answer else -1)
