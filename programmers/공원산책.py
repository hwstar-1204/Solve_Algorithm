def check_obstacle(park, sh, sw, eh, ew):
    if sh == eh:
        step = 1 if sw < ew else -1
        for w in range(sw+step, ew+step, step):
            if park[eh][w] == "X":
                return True
    else:
        start, end = min(sh,eh), max(sh,eh)
        step = 1 if sh < eh else -1
        for h in range(sh+step, eh+step, step):
            if park[h][ew] == "X":
                return True
    return False
    

def solution(park, routes):
    h, w = len(park), len(park[0])
    
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                nh, nw = i, j  # 시작점
                break
                
    direct = {"E": (0,1), "W": (0,-1), "N": (-1,0), "S": (1,0)}
    for route in routes:
        op, n = route.split(" ")
        next_h = nh + direct[op][0] * int(n)
        next_w = nw + direct[op][1] * int(n)

        if 0 <= next_h < h and 0 <= next_w < w:
            if not check_obstacle(park, nh, nw, next_h, next_w):
                nh = next_h
                nw = next_w

    return [nh, nw]
