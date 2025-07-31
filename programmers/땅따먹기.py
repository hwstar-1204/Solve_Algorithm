def solution(land):
    ans = 0
    before_vals = {"col": -1, "max_val": 0}
    
    for i in range(len(land)):
        now_vals = {"col": -1, "max_val": 0}
        for j in range(4):
            if before_vals["col"] == j:
                continue
            
            if now_vals["max_val"] <= land[i][j]:
                now_vals["max_val"] = land[i][j]
                now_vals["col"] = j
        
        ans += now_vals["max_val"]
        before_vals = now_vals
        
    return ans
                
