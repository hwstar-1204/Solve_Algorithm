from typing import List


def solution(n):
    answer = 0

    def backtrack(n, curr_row, batch_queens: List[int]):
        nonlocal answer
        if curr_row == n:
            answer += 1
            return

        for curr_col in range(n):
            if is_available(batch_queens, curr_row, curr_col):
                batch_queens[curr_row] = curr_col
                backtrack(n, curr_row+1, batch_queens)
                batch_queens[curr_row] = -1
    
    def is_available(batch_q_rows, curr_row, curr_col):
        for prev_row in range(curr_row):
            prev_col = batch_q_rows[prev_row]
            if prev_col == curr_col:  # 세로
                return False
            if abs(prev_col - curr_col) == abs(prev_row - curr_row):  # 대각선
                return False
            
        return True


    backtrack(n, 0, [-1] * n)  # 체스판 크기, 현재 탐색 열, 지금까지 놓은 퀀의 행 위치들
    return answer


n = 4
result = 2
res = solution(n)
assert res == result