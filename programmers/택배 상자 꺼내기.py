def solution(n, w, num):
    row, col = divmod(num - 1, w)
    if row % 2 == 1:
        col = w - col - 1
        
    top_row = (n - 1) // w
    cnt = top_row - row + 1
    
    real_col = w - col - 1 if top_row % 2 == 1 else col    
    same_col_top_num = (top_row * w + 1) + real_col
    
    # num의 같은 열 최대 행에 숫자가 없으면 -1 하고 return 
    if n < same_col_top_num:
        return cnt - 1
    return cnt